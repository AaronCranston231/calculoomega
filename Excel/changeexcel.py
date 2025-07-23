from openpyxl import load_workbook

excel_path = r"C:\Users\ivand\OneDrive\Escritorio\GUI_OMEGA\Cálculo_Omega_Final.xlsx"

try:
    wb = load_workbook(excel_path)
    sheet = wb.active  # o wb['NombreHoja']
    
    sheet['K14'].value = "Cierre de Ceja"  # Reemplaza con el valor de tu lista
    
    # Guardar los cambios
    wb.save(excel_path)
    print("si")

except Exception as e:
    print(f"Error: {e}")