import xlwings as xw

excel_path = r"C:\Users\Ulises\GUI_OMEGA\Calculo Tubulares.xlsx"

try:
    app = xw.App(visible=False)  # Excel en segundo plano
    wb = xw.Book(excel_path)
    sheet = wb.sheets['Pedido']  # Cambia al nombre de tu hoja
    valor = sheet.range('M7').value
    print(f"El valor en B8 es: {valor}")  # Devolverá 55
    wb.close()
    app.quit()
except Exception as e:
    print(f"Error: {e}")