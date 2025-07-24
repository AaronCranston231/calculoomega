

def generar_pdf_W(datos, plantilla_pdf=r"C:\Users\Ulises\GUI_OMEGA\Ordenestrabajo\ORDEN TRABAJO (3).pdf", 
               salida_pdf="orden_trabajoW_relleno.pdf",
               imagen_path=r"C:\Users\Ulises\GUI_OMEGA\GUI\Dibujos\TubularW_editada.jpg"):
    from PyPDF2 import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.utils import ImageReader
    import io

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

    # Insertar la imagen (ajusta las coordenadas y tamaño según necesites)
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

    with open(salida_pdf, "wb") as f:
        output.write(f)

