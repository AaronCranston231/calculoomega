def calcular_tubular_w(diam_tubo: str, watts: float, volts: float, ancho: float, largo_tub: float, largo2: float, tornillos: float = 80):
    import csv
    import numpy as np

    # Convertir diam_tubo a valor numérico (como en tu código original)
    if diam_tubo == "3/8":
        diam_tubo_val = 1
        dimension_diam_tubo = "3/8"
    elif diam_tubo == "1/2":
        diam_tubo_val = 2
        dimension_diam_tubo = "1/2"
    else:
        raise ValueError("Diámetro inválido. Usa '3/8' o '1/2'.")

    amps = watts / volts
    ohms = volts / amps

    # --- Cálculo de geometría (idéntico a tu código) ---
    if diam_tubo_val == 1:
        long_vuelta = (ancho - 8) / 3 + 8
        radio_interno = (long_vuelta / np.pi) - 0.8
        husillo = "2mm"
    else:
        long_vuelta = (ancho - 11) / 3 + 11
        radio_interno = (long_vuelta / np.pi) - 1.1
        husillo = "3mm"

    desarrollo_radio_interno = (long_vuelta - (radio_interno * 2)) * np.pi
    largo = largo_tub - (long_vuelta - 2 * (8 if diam_tubo_val == 1 else 11))
    largo2 = largo2 - long_vuelta
    desarrollo_tubo = (largo * 2) + (desarrollo_radio_interno * 3) + (largo2 * 2)

    # Ajuste de tornillos (igual que tu código)
    zf = tornillos - 20  
    zc = desarrollo_tubo - zf
    cortar_tubo = desarrollo_tubo * 0.88

    # --- Lectura del CSV (igual que tu código) ---
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

    # --- Búsqueda del calibre válido (igual que tu código) ---
    calibre_valido = None
    mejor_candidato = None
    menor_error = float("inf")

    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        ml = (ohms / ohm_alambre) * 1.2
        desarrollo_alambre = (2 + diam_alambre) * np.pi if diam_tubo_val == 1 else (3 + diam_alambre) * np.pi
        num_vueltas = ml * 1000 / desarrollo_alambre
        paso = zc / num_vueltas
        separacion = paso - diam_alambre
        bobina_sin_estirar = num_vueltas * diam_alambre

        # Rangos de separación (igual que tu código)
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
            print(f"✅ Calibre válido encontrado: {calibre}")  # Debug
            return {
                "zc": zc,
                "zf": zf,
                "watts": watts,
                "volts": volts,
                "amps": amps,
                "ohms": ohms,
                "ohm_alambre": ohm_alambre,
                "diam_tubo": dimension_diam_tubo,  # Usa el string "3/8" o "1/2"
                "diam_alambre": diam_alambre,
                "ml": ml,
                "radio_interno" : radio_interno,
                "largo_tubo": desarrollo_tubo,
                "calibre": calibre,
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
            error = abs(separacion - (min_sep if separacion < min_sep else max_sep))
            if error < menor_error:
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }

    # Si no se encontró calibre válido
    print(f"⚠️ Mejor candidato: Calibre {mejor_candidato['calibre']} (Separación: {mejor_candidato['separacion']:.2f})")
    return {
        "valido": False,
        "mejor_candidato": mejor_candidato,
        "amps": amps,
        "ohms": ohms
    }