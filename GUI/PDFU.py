import sys
import os

def get_resource_path(relative_path):
    """Obtener la ruta correcta para recursos en ejecutables"""
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generar_pdf_U(datos, 
                  plantilla_pdf=None, 
                  salida_pdf="orden_trabajo_relleno_U.pdf",
                  imagen_path=None):
    
    from PyPDF2 import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.utils import ImageReader
    import io
    import os 
    
    try:
        # Usar get_resource_path para archivos incluidos en el ejecutable
        if plantilla_pdf is None:
            plantilla_pdf = get_resource_path("ORDEN TRABAJO (3).pdf")
        if imagen_path is None:
            imagen_path = get_resource_path("Dibujos/TubularU_editada.jpg")

        print(f"Usando plantilla PDF: {plantilla_pdf}")
        print(f"Usando imagen: {imagen_path}")

        # Verificar que los archivos existen
        if not os.path.exists(plantilla_pdf):
            print(f"❌ Error: No se encontró la plantilla PDF en {plantilla_pdf}")
            # Mostrar archivos disponibles para debugging
            try:
                base_path = sys._MEIPASS
                print("Archivos PDF disponibles en _MEIPASS:")
                for file in os.listdir(base_path):
                    if file.endswith('.pdf'):
                        print(f"  - {file}")
            except:
                print("Archivos PDF disponibles en directorio actual:")
                for file in os.listdir("."):
                    if file.endswith('.pdf'):
                        print(f"  - {file}")
            raise FileNotFoundError(f"Plantilla PDF no encontrada: {plantilla_pdf}")

        # Para el directorio de salida, usar el directorio actual (no _MEIPASS)
        BASE_DIR = os.path.abspath(".")
        
        # 📁 Crear subdirectorio para los PDFs si no existe
        carpeta_salida = os.path.join(BASE_DIR, "ordenes_de_trabajo_U")
        os.makedirs(carpeta_salida, exist_ok=True)

        # 📄 Ruta final del PDF dentro de la nueva carpeta
        ruta_salida_pdf = os.path.join(carpeta_salida, salida_pdf)

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # 📝 Insertar texto
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

        # 🖼 Insertar imagen
        try:
            if os.path.exists(imagen_path):
                img = ImageReader(imagen_path)
                can.drawImage(img, 50, 10, width=500, height=400, preserveAspectRatio=True)
                print(f"✅ Imagen insertada correctamente: {imagen_path}")
            else:
                print(f"⚠️ Advertencia: Imagen no encontrada en {imagen_path}")
        except Exception as e:
            print(f"❌ Error al insertar la imagen: {e}")

        can.save()
        packet.seek(0)

        existing_pdf = PdfReader(plantilla_pdf)
        new_pdf = PdfReader(packet)
        output = PdfWriter()

        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        with open(ruta_salida_pdf, "wb") as f:
            output.write(f)

        print(f"✅ PDF guardado exitosamente en: {ruta_salida_pdf}")

    except Exception as e:
        print(f"❌ Error completo en generar_pdf_U: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

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
    generar_pdf_U(datos_ejemplo)