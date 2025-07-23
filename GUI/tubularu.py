def calcular_tubular_u(diam_tubo: str, watts: float, volts: float, ancho: float, largo: float, tornillos: float = 70):
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

    # Cálculo de desarrollo tubular
    if diam_tubo_val == 1:
        radio_interno = ((ancho - 8) * np.pi) / 2
        largo_efectivo = largo - 16
        desarrollo_tubo = largo_efectivo * 2 + radio_interno
        husillo = "2mm"
    else:
        radio_interno = ((ancho - 11) * np.pi) / 2
        largo_efectivo = largo - 22
        desarrollo_tubo = largo_efectivo * 2 + radio_interno
        husillo = "3mm"

    cortar_tubo = desarrollo_tubo * 0.88
    zf = (tornillos - 20) * 2
    zc = desarrollo_tubo - zf

    # Leer tabla de calibres
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

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
                "ohm_alambre": ohm_alambre,
                "diam_tubo": diam_tubo,
                "diam_alambre": diam_alambre,
                "ml": ml,
                "largo_tubo": desarrollo_tubo,
                "calibre": calibre,
                "desarrollo_alambre": desarrollo_alambre,
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
        "ohms": ohms
        
    }
