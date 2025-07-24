import sys
import os
import csv

def get_resource_path(relative_path):
    """Obtener la ruta correcta para recursos en ejecutables"""
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def calcular_tubular_u(diam_tubo: str, watts: float, volts: float, ancho: float, largo: float, tornillos: float ):
    import csv
    import numpy as np

    if diam_tubo == "3/8":
        diam_tubo_val = 1
    elif diam_tubo == "1/2":
        diam_tubo_val = 2
    else:
        raise ValueError("Diámetro inválido. Usa '3/8' o '1/2'.")

    amps = watts / volts
    ohms = volts / amps
    ohms_tolerancia_arriba = ohms *1.05
    ohms_tolerancia_abajo = ohms *0.95

    # Cálculo de desarrollo tubular
    if diam_tubo_val == 1:
        long_vuelta = ((ancho - 8) * np.pi) / 2
        radio_interno = (long_vuelta/np.pi) - 0.8
        print(f'radio interno : {radio_interno}')
        print(f'largo : {largo}')
        largo_efectivo = float(largo - 16)
        print(f'largo_efectivo : {largo_efectivo}')
        desarrollo_tubo = float(largo_efectivo*2 + long_vuelta)
        print(f'desarrollo_tubo : {desarrollo_tubo}')
        husillo = "2mm"
        
    else:
        long_vuelta = ((ancho - 11) * np.pi) / 2
        radio_interno = (long_vuelta/np.pi) - 1.1

        largo_efectivo = largo - 22
        desarrollo_tubo = largo_efectivo * 2 + radio_interno
        husillo = "3mm"

    cortar_tubo = desarrollo_tubo - (desarrollo_tubo*0.12)
    zf = (tornillos - 20) * 2
    zc = desarrollo_tubo - zf

    # Leer tabla de calibres
    datos = []
    csv_path = get_resource_path("tabla_calibres.csv")
    print(f"Buscando CSV en: {csv_path}")  # Para debugging
    
    try:
        with open(csv_path, newline='') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                fila["Calibre"] = int(fila["Calibre"])
                fila["ESPEC"] = float(fila["ESPEC"])
                fila["Ohms"] = float(fila["Ohms"])
                datos.append(fila)
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo CSV en {csv_path}")
        # Verificar qué archivos están disponibles
        try:
            base_path = sys._MEIPASS
            print("Archivos disponibles en _MEIPASS:")
            for file in os.listdir(base_path):
                print(f"  - {file}")
        except:
            print("Archivos disponibles en directorio actual:")
            for file in os.listdir("."):
                print(f"  - {file}")
        
        # Retornar valores por defecto para que no crashee
        return {
            "valido": False,
            "mensaje": "Error: archivo CSV no encontrado",
            "amps": amps,
            "ohms": ohms,
            "ohms_tol_ab": ohms_tolerancia_abajo,
            "ohms_tol_ar": ohms_tolerancia_arriba,
            "mejor_candidato": None
        }

    # Variables para guardar mejor resultado
    calibre_valido = None
    mejor_candidato = None
    menor_error = float("inf")

    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        ml = (ohms / ohm_alambre) * 1.2
        if diam_tubo_val == 1:
            desarrollo_alambre = (2 + diam_alambre) * np.pi
        else:
            desarrollo_alambre = (3 + diam_alambre) * np.pi

        num_vueltas = ml * 1000 / desarrollo_alambre
        paso = zc / num_vueltas
        separacion = paso - diam_alambre
        bobina_sin_estirar = num_vueltas * diam_alambre

        # Rango de separación por calibre
        if 20 <= calibre <= 26:
            min_sep, max_sep = 1.0, 1.3
            ohms_bobina = ohms * 1.2
        elif 27 <= calibre <= 30:
            min_sep, max_sep = 0.9, 1.4
            ohms_bobina = ohms * 1.3
        elif 31 <= calibre <= 35:
            min_sep, max_sep = 0.7, 0.9
            ohms_bobina = ohms * 1.5
        else:
            continue

        if min_sep <= separacion <= max_sep:
            calibre_valido = calibre
            return {
                "zc": zc,
                "zf": zf,
                "watts": watts,
                "volts": volts,
                "amps": amps,
                "ohms": ohms,
                "ohms_tol_ar" : ohms_tolerancia_arriba,
                "ohms_tol_ab" : ohms_tolerancia_abajo,
                "ohm_alambre": ohm_alambre,
                "diam_tubo": diam_tubo,
                "diam_alambre": diam_alambre,
                "ml": ml,
                "largo_tubo": desarrollo_tubo,
                "calibre": calibre,
                "desarrollo_alambre": desarrollo_alambre,
                "radio_interno" : radio_interno,
                "num_vueltas": num_vueltas,
                "paso": paso,
                "separacion": separacion,
                "cortar_tubo": cortar_tubo,
                "husillo": husillo,
                "bobina_ohms": ohms_bobina,
                "bobina_sin_estirar": bobina_sin_estirar,
                "valido": True
            }

        else:
            error = abs(separacion - min_sep if separacion < min_sep else separacion - max_sep)
            if error < menor_error:
                menor_error = error
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }

    # Si ningún calibre fue válido
    return {
        "valido": False,
        "mejor_candidato": mejor_candidato,
        "amps": amps,
        "ohms": ohms,
        "ohms_tol_ab": ohms_tolerancia_abajo,
        "ohms_tol_ar": ohms_tolerancia_arriba
    }