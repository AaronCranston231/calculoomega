import xlwings as xw
import csv
import numpy as np

excel_path = r"C:\Users\Ulises\GUI_OMEGA\Calculo\Calculo Tubulares.xlsx"

# Abrir Excel en segundo plano
app = xw.App(visible=False)
wb = xw.Book(excel_path)
tipo_tubular = input("selecione el tipo de tubular que quiere: \n 1. Recta ; \n 2. Tubular U ; \n 3. Tubular W ;  \n 4. Tubular con tapon ;\n Escriba Solo el numero : ")
zc = 0 
zf = 0 

if tipo_tubular == "1" : 
    sheet = wb.sheets['TUBULAR R'] # Cambiar nombre en el excel a Tublar Recta
    diam_tubo = sheet.range('I10').value
    zc = sheet.range('C11').value
    largo_tub = sheet.range('C21').value
    #largo_tub = 0
    Ohm_resis = sheet.range('C18').value
    #zc = float(64.5)
    # Leer tabla de calibres desde CSV
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

    # Función de validación de separación por calibre
    def validar_separacion(calibre, separacion):
        if 20 <= calibre <= 26:
            return 1.0 <= separacion <= 1.3
        elif 27 <= calibre <= 30:
            return 0.9 <= separacion <= 1.4
        elif 31 <= calibre <= 35:
            return 0.7 <= separacion <= 0.9
        else:
            return False

    # Buscar el mejor calibre (válido o más cercano)
    calibre_valido = None
    mejor_candidato = None
    menor_error = float('inf')

    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        # Calcular ml requerido
        ml = (Ohm_resis / ohm_alambre) * 1.2

        # Cálculo de desarrollo según diámetro del tubo
        if diam_tubo == "3/8'":
            desarrollo = float((2 + diam_alambre) * 3.14)
        elif diam_tubo == "1/2'":
            desarrollo = float((3 + diam_alambre) * 3.14)
        else:
            desarrollo = 1  # evitar división entre cero

        num_vueltas = ml * 1000 / desarrollo
        paso = zc * 10 / num_vueltas
        separacion = paso - diam_alambre
        
        
        print("__________________________-")
        print(f'diam tubo : {diam_tubo}')
        print(f'ohm resis : {Ohm_resis} y ohm_alambre : {ohm_alambre}')
        print(f'Diam alambre : {diam_alambre}')
        print(f'ml son : {ml}')
        print(f'desarrollo : {desarrollo}')
        print(f'Calibre: {calibre}')
        print(f'num vueltas : {num_vueltas}, paso : {paso}, separacion : {separacion}')
        print("__________________________-")


        # Validar separación
        if 20 <= calibre <= 26:
            min_sep, max_sep = 1.0, 1.3
        elif 27 <= calibre <= 30:
            min_sep, max_sep = 0.9, 1.4
        elif 31 <= calibre <= 35:
            min_sep, max_sep = 0.7, 0.9
        else:
            continue  # fuera de rango

        if min_sep <= separacion <= max_sep:
            calibre_valido = calibre
            print(f"✅ Calibre válido encontrado: {calibre}")
            print(f"📏 Separación: {separacion:.3f} mm")
            break
        else:
            # Calcular qué tan lejos está del rango permitido
            if separacion < min_sep:
                error = min_sep - separacion
            elif separacion > max_sep:
                error = separacion - max_sep
            else:
                error = 0  

            if error < menor_error:
                menor_error = error
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }

    # Si no se encontró ningún calibre válido
    if calibre_valido is None:
        print("❌ Ningún calibre cumplió exactamente.")
        print(f"🟡 Pero el más cercano fue: Calibre {mejor_candidato['calibre']} con separación {mejor_candidato['separacion']:.3f} mm (error: {mejor_candidato['error']:.3f})")
        
        
if tipo_tubular == "2" : 
    diam_tubo = int(input ("Seleccione el diametro de tubo de la resistencia : \n 1.- 3/8' , 2.- 1/2' \n Escriba la opcion : "))

    # Leer tabla de calibres desde CSV
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

    # Función de validación de separación por calibre
    def validar_separacion(calibre, separacion):
        if 20 <= calibre <= 26:
            return 1.0 <= separacion <= 1.3
        elif 27 <= calibre <= 30:
            return 0.9 <= separacion <= 1.4
        elif 31 <= calibre <= 35:
            return 0.7 <= separacion <= 0.9
        else:
            return False

    # Buscar el primer calibre que cumple la validación
    # Buscar el mejor calibre (válido o más cercano)
    calibre_valido = None
    mejor_candidato = None
    menor_error = float('inf')
    
    
    
   # '''
    
    #Desde aqui se esta modificando !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    watts = float(input("Escriba los watts que quiere en la resistencia : \n"))
    volts = float(input("Escriba los volts que quiere en la resistencia :  \n"))
    amps = watts/volts
    #print(f'Los amps son: {amps} \n')
    ohms = volts/amps
    #print(f' los ohms son : {ohms}') 
    
    
    #### HASTA AQUI TO 'DO BIEN 
     
     
    ancho_tubular = float(input("Escriba el ancho de la resistencia en mm : "))
    largo_tub = float(input("Escriba el largo de la resistencia de un solo lado  en mm: "))
    tornillos = float(input("Escriba el tama;o de los tornillos en mm : "))
        
    ## Calculo longitud Resistencia
        
    
    if diam_tubo == 1:
        radio_interno = float((ancho_tubular - 8)*np.pi/2) #AQUI BIEN
        
        largo = float(largo_tub - 8-8)
        
        desarrollo_tubo = float(largo*2 + radio_interno)
        
        zf = (tornillos - 20)*2
        zc = desarrollo_tubo - zf 
        cortar_tubo = desarrollo_tubo - (desarrollo_tubo*0.12)
        husillo = "2mm"
       
    elif diam_tubo == 2:
        radio_interno = float((ancho_tubular - 11)*np.pi/2) #AQUI BIEN
        print(f'Radio interno : {radio_interno}\n')
        
        largo = float(largo_tub - 11-11)
        print(f'largotubular : {largo}') # HASTA AQUI BIEN
        
        desarrollo_tubo = float(largo*2 + radio_interno)
        print(f'desarrollo tubular : {desarrollo_tubo}') # HASTA AQUI BIEN 
        
        zf = (tornillos - 20)*2
        zc = desarrollo_tubo - zf
        cortar_tubo = desarrollo_tubo - (desarrollo_tubo*0.12)
        husillo = "3mm"
          
    else:
        pass 
    
    
    
    
    #'''
    
    
    '''
    
    #ESTO DE AQUI FUNCIONA
    
    zc = float(63.512)
    largo_tub = float(73.512)
    Ohm_resis = 96
    
    
    
    '''
    
    
    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        # Calcular ml requerido
        ml = (ohms / ohm_alambre) * 1.2
        # Cálculo de desarrollo según diámetro del tubo
        if diam_tubo == 1:
            desarrollo = float((2 + diam_alambre) * 3.14)
            dimension_diam_tubo = "3/8"
        elif diam_tubo == 2:
            desarrollo = float((3 + diam_alambre) * 3.14)
            dimension_diam_tubo = "1/2"
        else:
            print("PUSO MAL LOS DATOS Y EL CALCULO NO FUNCIONA")

        num_vueltas = ml * 1000 / desarrollo 
        paso = zc / num_vueltas
        separacion = paso - diam_alambre
        bobina_sin_estirar = num_vueltas*diam_alambre
        

        # Validar separación
        if 20 <= calibre <= 26:
            min_sep, max_sep = 1.0, 1.3
            ohms_bobina = ohms *1.2
        elif 27 <= calibre <= 30:
            min_sep, max_sep = 0.9, 1.4
            ohms_bobina = ohms * 1.3
        elif 31 <= calibre <= 35:
            min_sep, max_sep = 0.7, 0.9
            ohms_bobina = ohms*1.5
        else:
            continue  # fuera de rango

        if min_sep <= separacion <= max_sep:
            calibre_valido = calibre
            print(f'!!!!!!!!!!!!!!!!!CALIBRE ENCONTRADO QUE CUMPLE CON REQUISITOS !!!!!! \n')
            print(f'\n')
            print("__________________________")
            print(f'\n')
            print(f'zc es : {zc} mm')
            print(f'Zona Fria : {zf/2} por cada lado o {zf} por ambos lados')
            print(f'Watts : {watts} w')
            print(f'Volts : {volts} v')
            print(f'Amps : {amps} A')
            print(f'ohm resis : {ohms} ohms')
            print(f'y ohm_alambre : {ohm_alambre}')
            print(f'Diametro final tubo : {dimension_diam_tubo} "')
            print(f'Diam alambre : {diam_alambre}')
            print(f'ml son : {ml}')
            print(f'Largo : {desarrollo_tubo} mm')
            print(f'Calibre: {calibre}')
            print(f"desarrollo alambre : {desarrollo}")
            print(f'num vueltas : {num_vueltas}, paso : {paso}, separacion : {separacion}')
            print(f'Cortar tubo a : {cortar_tubo} mm')
            print(f'Husillo de : {husillo} ')
            print(f'Bobina a : {ohms_bobina } ohms')
            print(f'Long bobina sin estirar : {bobina_sin_estirar} mm')
            print("__________________________ \n")
            
            break
        else:
            # Calcular qué tan lejos está del rango permitido
            if separacion < min_sep:
                error = min_sep - separacion
            elif separacion > max_sep:
                error = separacion - max_sep
            else:
                error = 0  

            if error < menor_error:
                menor_error = error
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }



    # Si no se encontró ningún calibre válido
    if calibre_valido is None:
        print("❌ Ningún calibre cumplió exactamente.")
        print(f"🟡 Pero el más cercano fue: Calibre {mejor_candidato['calibre']} con separación {mejor_candidato['separacion']:.3f} mm (error: {mejor_candidato['error']:.3f})")


if tipo_tubular == "3" : 
    diam_tubo = int(input ("Seleccione el diametro de tubo de la resistencia : \n 1.- 3/8' , 2.- 1/2' \n Escriba la opcion : "))

    # Leer tabla de calibres desde CSV
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

    # Función de validación de separación por calibre
    def validar_separacion(calibre, separacion):
        if 20 <= calibre <= 26:
            return 1.0 <= separacion <= 1.3
        elif 27 <= calibre <= 30:
            return 0.9 <= separacion <= 1.4
        elif 31 <= calibre <= 35:
            return 0.7 <= separacion <= 0.9
        else:
            return False


    calibre_valido = None
    mejor_candidato = None
    menor_error = float('inf')
    
    
    watts = float(input("Escriba los watts que quiere en la resistencia : \n"))
    volts = float(input("Escriba los volts que quiere en la resistencia :  \n"))
    amps = watts/volts
    #print(f'Los amps son: {amps} \n')
    ohms = volts/amps
    #print(f' los ohms son : {ohms}') 

     
    ancho_tubular = float(input("Escriba el ancho de la resistencia en mm : "))
    largo_tub = float(input("Escriba el largo de la resistencia de un solo lado  en mm: "))
    tornillos = float(input("Escriba el tama;o de los tornillos en mm : "))
    largo2 = float(input(f"Escriba el tama;o del largo desde la punta donde esta la w hasta el final de la tubular W : "))
        
    ## Calculo longitud Resistencia
        
    long_vuelta = 0
    
    if diam_tubo == 1:
        long_vuelta = float((ancho_tubular-8)/3) + 8 
        print(f'LONG VUELTA : {long_vuelta}')

        radio_interno = float(long_vuelta/np.pi)- 0.8 
        print(f'RADIO INTERNO : {radio_interno}')

        desarrollo_radio_interno = (long_vuelta-(radio_interno*2))*np.pi
        print(f'DESARROLLO RADIO INTERNO : {desarrollo_radio_interno}')

        largo = long_vuelta -8-8
        largo = largo_tub - largo
        print(f'LARGO :  {largo}')
        largo2 = largo2 - long_vuelta
        print(f'LARGO 2 : {largo2}')
        desarrollo_tubo = (largo*2) + (desarrollo_radio_interno*3) + (largo2*2)
        print(f'DESARROLLO TUBO  : {desarrollo_tubo}')
        zf = tornillos - 20 
        zc = desarrollo_tubo - zf 
        cortar_tubo = desarrollo_tubo        
         
       
    elif diam_tubo == 2:
        long_vuelta = float((ancho_tubular-11)/3) + 11 
        print(f'LONG VUELTA : {long_vuelta}')

        radio_interno = float(long_vuelta/np.pi)- 1.1 
        print(f'RADIO INTERNO : {radio_interno}')

        desarrollo_radio_interno = (long_vuelta-(radio_interno*2))*np.pi
        print(f'DESARROLLO RADIO INTERNO : {desarrollo_radio_interno}')

        largo = long_vuelta -11-11
        largo = largo_tub - largo
        print(f'LARGO :  {largo}')
        largo2 = largo2 - long_vuelta
        print(f'LARGO 2 : {largo2}')
        desarrollo_tubo = (largo*2) + (desarrollo_radio_interno*3) + (largo2*2)
        print(f'DESARROLLO TUBO  : {desarrollo_tubo}')
        zf = tornillos - 20 
        zc = desarrollo_tubo - zf 
        cortar_tubo = desarrollo_tubo             
    else:
        pass 
    
    
    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        # Calcular ml requerido
        ml = (ohms / ohm_alambre) * 1.2
        # Cálculo de desarrollo según diámetro del tubo
        if diam_tubo == 1:
            desarrollo = float((2 + diam_alambre) * 3.14)
            dimension_diam_tubo = "3/8"
        elif diam_tubo == 2:
            desarrollo = float((3 + diam_alambre) * 3.14)
            dimension_diam_tubo = "1/2"
        else:
            print("PUSO MAL LOS DATOS Y EL CALCULO NO FUNCIONA")

        num_vueltas = ml * 1000 / desarrollo 
        paso = zc / num_vueltas
        separacion = paso - diam_alambre
        bobina_sin_estirar = num_vueltas*diam_alambre
        

        # Validar separación
        if 20 <= calibre <= 26:
            min_sep, max_sep = 1.0, 1.3
            ohms_bobina = ohms *1.2
        elif 27 <= calibre <= 30:
            min_sep, max_sep = 0.9, 1.4
            ohms_bobina = ohms * 1.3
        elif 31 <= calibre <= 35:
            min_sep, max_sep = 0.7, 0.9
            ohms_bobina = ohms*1.5
        else:
            continue  # fuera de rango

        if min_sep <= separacion <= max_sep:
            calibre_valido = calibre
            print(f'!!!!!!!!!!!!!!!!!CALIBRE ENCONTRADO QUE CUMPLE CON REQUISITOS !!!!!! \n')
            print(f'\n')
            print("__________________________")
            print(f'\n')
            print(f'zc es : {zc} mm')
            print(f'Zona Fria : {zf/2} por cada lado o {zf} por ambos lados')
            print(f'Watts : {watts} w')
            print(f'Volts : {volts} v')
            print(f'Amps : {amps} A')
            print(f'ohm resis : {ohms} ohms')
            #print(f'y ohm_alambre : {ohm_alambre}')
            print(f'Diametro final tubo : {dimension_diam_tubo} "')
            #print(f'Diam alambre : {diam_alambre}')
            print(f'radio : {radio_interno}')
            print(f'ml son : {ml}')
            print(f'Largo : {desarrollo_tubo} mm')
            print(f'Calibre: {calibre}')
            print(f'num vueltas : {num_vueltas}, paso : {paso}, separacion : {separacion}')
            print(f'Cortar tubo a : {cortar_tubo} mm')
            #print(f'Husillo de : {husillo} ')
            print(f'Bobina a : {ohms_bobina } ohms')
            print(f'Long bobina sin estirar : {bobina_sin_estirar} mm')
            #print(f'Separacion : {separacion} mm')

            print("__________________________ \n")
            
            break
        else:
            # Calcular qué tan lejos está del rango permitido
            if separacion < min_sep:
                error = min_sep - separacion
            elif separacion > max_sep:
                error = separacion - max_sep
            else:
                error = 0  

            if error < menor_error:
                menor_error = error
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }



    # Si no se encontró ningún calibre válido
    if calibre_valido is None:
        print("❌ Ningún calibre cumplió exactamente.")
        print(f"🟡 Pero el más cercano fue: Calibre {mejor_candidato['calibre']} con separación {mejor_candidato['separacion']:.3f} mm (error: {mejor_candidato['error']:.3f})")


if tipo_tubular == "4" : 
    diam_tubo = int(input ("Seleccione el diametro de tubo de la resistencia : \n 1.- 3/8' , 2.- 1/2' \n Escriba la opcion : "))

    # Leer tabla de calibres desde CSV
    datos = []
    with open("tabla_calibres.csv", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for fila in reader:
            fila["Calibre"] = int(fila["Calibre"])
            fila["ESPEC"] = float(fila["ESPEC"])
            fila["Ohms"] = float(fila["Ohms"])
            datos.append(fila)

    # Función de validación de separación por calibre
    def validar_separacion(calibre, separacion):
        if 20 <= calibre <= 26:
            return 1.0 <= separacion <= 1.3
        elif 27 <= calibre <= 30:
            return 0.9 <= separacion <= 1.4
        elif 31 <= calibre <= 35:
            return 0.7 <= separacion <= 0.9
        else:
            return False

    # Buscar el primer calibre que cumple la validación
    # Buscar el mejor calibre (válido o más cercano)
    calibre_valido = None
    mejor_candidato = None
    menor_error = float('inf')
    
    
    
   # '''
    
    #Desde aqui se esta modificando !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    watts = float(input("Escriba los watts que quiere en la resistencia : \n"))
    volts = float(input("Escriba los volts que quiere en la resistencia :  \n"))
    watts2 = watts/3
    volts2 = volts/1.73
    amps_general = 0
    amps_tubular = 0
    ohms_general = 0
    ohms_tubular = 0
     
    ancho_tubular = float(input("Escriba el ancho de la resistencia en mm : "))
    largo_tub = float(input("Escriba el largo de la resistencia de un solo lado  en mm: "))
    tornillos = float(input("Escriba el tama;o de los tornillos en mm : "))
    largo_total_tub = largo_tub + 35 + 10 
    conexion = None
    
    if (volts >= 440 and largo_tub < 500) : 
        conexion = "ESTRELLA"
        amps_general = watts/volts/1.73
        ohms_general = (volts*volts*2)/watts
        amps_tubular = watts2/volts2 
        ohms_tubular = volts2/amps_tubular
    elif (200 <= volts <=250 and largo_tub <= 300): 
        conexion = "ESTRELLA"
        amps_general = watts/volts/1.73
        ohms_general = (volts*volts*2)/watts
        amps_tubular = watts2/volts2 
        ohms_tubular = volts2/amps_tubular
    else:
        conexion = "DELTA"     
        amps_general = watts/volts/1.73
        ohms_general = (volts*volts*2)/watts
        amps_tubular = watts2/volts 
        ohms_tubular = volts/amps_tubular
    
    print(conexion)
    print(f'Amps general : {amps_general}, ohms general : {ohms_general}, amps_tubular : {amps_tubular}, ohms tubular: {ohms_tubular}')
    
    if diam_tubo == 1:
        radio_interno = float((ancho_tubular - 8)*np.pi/2) #AQUI BIEN
        
        largo = float(largo_total_tub - 8-8)
        
        desarrollo_tubo = float(largo*2 + radio_interno)
        
        zf = (tornillos - 20)*2
        zc = desarrollo_tubo - zf 
        cortar_tubo = desarrollo_tubo - (desarrollo_tubo*0.12)
        husillo = "2mm"
       
    elif diam_tubo == 2:
        radio_interno = float((ancho_tubular - 11)*np.pi/2) #AQUI BIEN
        
        largo = float(largo_total_tub - 11-11)
        
        desarrollo_tubo = float(largo*2 + radio_interno)
        
        zf = (tornillos - 20)*2
        zc = desarrollo_tubo - zf
        cortar_tubo = desarrollo_tubo - (desarrollo_tubo*0.12)
        husillo = "3mm"          
    else:
        pass 
    
    
    for fila in datos:
        calibre = fila["Calibre"]
        diam_alambre = fila["ESPEC"]
        ohm_alambre = fila["Ohms"]

        # Calcular ml requerido
        ml = (ohms_tubular / ohm_alambre) * 1.2
        # Cálculo de desarrollo según diámetro del tubo
        if diam_tubo == 1:
            desarrollo = float((2 + diam_alambre) * 3.14)
            dimension_diam_tubo = "3/8"
        elif diam_tubo == 2:
            desarrollo = float((3 + diam_alambre) * 3.14)
            dimension_diam_tubo = "1/2"
        else:
            print("PUSO MAL LOS DATOS Y EL CALCULO NO FUNCIONA")

        num_vueltas = ml * 1000 / desarrollo 
        paso = zc / num_vueltas
        separacion = paso - diam_alambre
        bobina_sin_estirar = num_vueltas*diam_alambre
        

        # Validar separación
        if 20 <= calibre <= 26:
            min_sep, max_sep = 1.0, 1.3
            ohms_bobina = ohms_tubular *1.2
        elif 27 <= calibre <= 30:
            min_sep, max_sep = 0.9, 1.4
            ohms_bobina = ohms_tubular * 1.3
        elif 31 <= calibre <= 35:
            min_sep, max_sep = 0.7, 0.9
            ohms_bobina = ohms_tubular*1.5
        else:
            continue  # fuera de rango

        if min_sep <= separacion <= max_sep:
            calibre_valido = calibre
            print("\n✅✅✅ ¡CALIBRE ENCONTRADO QUE CUMPLE CON LOS REQUISITOS! ✅✅✅\n")
            print("🟢──────────────────────────────────────────────────────────────────🟢")
            print(f"🟢 ➤ zc: {zc} mm")
            print(f"🟢 ➤ Zona Fría: {zf/2} mm por lado (total: {zf} mm)")
            print(f"🟢 ➤ Watts: {watts} W     Volts: {volts} V")
            print(f"🟢 ➤ Amperaje general: {amps_general:.2f} A")
            print(f"🟢 ➤ Amperaje tubular: {amps_tubular:.2f} A")
            print(f"🟢 ➤ Resistencia general: {ohms_general:.3f} Ω")
            print(f"🟢 ➤ Resistencia tubular: {ohms_tubular:.3f} Ω")
            print(f"🟢 ➤ Ohm por metro de alambre: {ohm_alambre:.6f} Ω/m")
            print(f"🟢 ➤ Diámetro final del tubo: {dimension_diam_tubo}\"")
            print(f"🟢 ➤ Diámetro del alambre: {diam_alambre}")
            print(f"🟢 ➤ Metros lineales necesarios: {ml:.2f} m")
            print(f"🟢 ➤ Desarrollo del alambre: {desarrollo:.3f} mm")
            print(f"🟢 ➤ Número de vueltas: {num_vueltas:.1f}")
            print(f"🟢 ➤ Paso: {paso:.3f} mm")
            print(f"🟢 ➤ Separación entre espiras: {separacion:.3f} mm ✅")
            print(f"🟢 ➤ Calibre seleccionado: {calibre}")
            print(f"🟢 ➤ Largo del tubo desarrollado: {desarrollo_tubo} mm")
            print(f"🟢 ➤ Cortar tubo a: {cortar_tubo} mm")
            print(f"🟢 ➤ Husillo: {husillo}")
            print(f"🟢 ➤ Bobina a: {ohms_bobina:.3f} Ω")
            print(f"🟢 ➤ Longitud bobina sin estirar: {bobina_sin_estirar:.2f} mm")
            print("🟢──────────────────────────────────────────────────────────────────🟢\n")
            break
        else:
            # Calcular qué tan lejos está del rango permitido
            if separacion < min_sep:
                error = min_sep - separacion
            elif separacion > max_sep:
                error = separacion - max_sep
            else:
                error = 0  

            if error < menor_error:
                menor_error = error
                mejor_candidato = {
                    "calibre": calibre,
                    "separacion": separacion,
                    "error": error
                }
  


    # if calibre_valido is not None:
    #     print("✅✅ Calibre encontrado exitosamente:")
    #     print(f"🟢 ➤ Calibre seleccionado: {calibre_valido['calibre']}")
    #     print(f"🟢 ➤ Separación obtenida: {calibre_valido['separacion']:.3f} mm")
    #     print(f"🟢 ➤ Error: {calibre_valido['error']:.3f} mm")
        
    # Si no se encontró ningún calibre válido
    
    if calibre_valido is None:
        print("❌ Ningún calibre cumplió exactamente.")
        print(f"🟡 Pero el más cercano fue: Calibre {mejor_candidato['calibre']} con separación {mejor_candidato['separacion']:.3f} mm (error: {mejor_candidato['error']:.3f})")


wb.close()
app.quit()