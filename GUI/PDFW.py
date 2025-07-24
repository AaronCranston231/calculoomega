def generar_pdf_W(datos, 
                  plantilla_pdf=None, 
                  salida_pdf="orden_trabajoW_relleno.pdf",
                  imagen_path=None):
    from PyPDF2 import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.utils import ImageReader
    import io
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if plantilla_pdf is None:
        plantilla_pdf = os.path.join(BASE_DIR, "ORDEN TRABAJO (3).pdf")
    if imagen_path is None:
        imagen_path = os.path.join(BASE_DIR, "Dibujos", "TubularW_editada.jpg")

    # Crear carpeta de salida si no existe
    carpeta_salida = os.path.join(BASE_DIR, "ordenes_trabajo_W")
    os.makedirs(carpeta_salida, exist_ok=True)

    salida_pdf_path = os.path.join(carpeta_salida, salida_pdf)

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Insertar datos de texto
    can.drawString(125, 760, datos.get("cliente", ""))
    can.drawString(125, 740, datos.get("orden", ""))
    can.drawString(125, 720, datos.get("unidades", ""))
    can.drawString(125, 680, datos.get("elementos_por_unidad", ""))
    can.drawString(420, 750, datos.get("fecha", ""))
    can.drawString(420, 730, datos.get("piezas", ""))
    can.drawString(420, 710, datos.get("entrega", ""))

    can.drawString(125, 637, datos.get("watts", ""))
    can.drawString(125, 607, datos.get("volts", ""))
    can.drawString(125, 579, datos.get("Ampers", ""))
    can.drawString(125, 553, datos.get("ohms", ""))
    can.drawString(185, 553, datos.get("ohms_tol_ar", "") + ", " + datos.get("ohms_tol_ab", ""))

    can.drawString(450, 637, datos.get("Material", ""))
    can.drawString(450, 607, datos.get("Diametro", ""))
    can.drawString(450, 579, datos.get("largo", ""))

    can.drawString(200, 485, datos.get("calibre", ""))
    can.drawString(200, 457, datos.get("Husillo", ""))
    can.drawString(200, 430, datos.get("bobina a", ""))
    can.drawString(200, 400, datos.get("Long Bobina", ""))

    can.drawString(485, 475, datos.get("Cortar a", ""))
    can.drawString(486, 445, datos.get("Diametro", ""))

    # Insertar la imagen
    try:
        img = ImageReader(imagen_path)
        can.drawImage(img, 50, 10, width=500, height=400, preserveAspectRatio=True)
    except Exception as e:
        print(f"Error al insertar la imagen: {e}")

    can.save()
    packet.seek(0)

    existing_pdf = PdfReader(plantilla_pdf)
    new_pdf = PdfReader(packet)
    output = PdfWriter()

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    with open(salida_pdf_path, "wb") as f:
        output.write(f)


if __name__ == "__main__":
    # Datos de ejemplo para prueba
    datos_ejemplo = {
        "cliente": "Cliente Ejemplo",
        "orden": "ORD-1234",
        "fecha": "2023-11-15",
        "ohms_tol_ar" : "234",
        "ohms_tol_ab" : "433",
        # Agrega aquí el resto de tus campos
    }
    generar_pdf_W(datos_ejemplo)