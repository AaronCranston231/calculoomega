from openpyxl import load_workbook

excel_path = r"C:\Users\Ulises\GUI_OMEGA\Calculo Tubulares.xlsx"

try:
    # Cargar el libro de trabajo
    wb = load_workbook(excel_path)
    
    # Seleccionar la hoja (cambia 'Hoja1' por el nombre de tu hoja)
    sheet = wb['Pedido']
    
    # Escribir un número en una celda específica (por ejemplo, B1)
    sheet['M7'] = 225  
    
    # Guardar los cambios
    wb.save(excel_path)
    
    print("Número escrito correctamente en el archivo Excel.")

except FileNotFoundError:
    print("Error: No se pudo encontrar el archivo Excel en la ruta especificada.")
except Exception as e:
    print(f"Error al leer/escribir el archivo: {e}")