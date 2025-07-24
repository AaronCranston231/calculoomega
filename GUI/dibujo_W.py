from PIL import Image, ImageDraw, ImageFont
import os
import sys

def agregar_texto_centradoW(largo_value, 
                            ancho_value,
                            largo2_value,
                            radio_value):
   
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Cuando está empaquetado
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Ruta relativa a la imagen original
    ruta_imagen_original = os.path.join(base_path, "Dibujos", "TUBULARWFINAL.jpg")
   
    try:
        imagen_original = Image.open(ruta_imagen_original)
    except FileNotFoundError:
        print(f"No se pudo encontrar la imagen en: {ruta_imagen_original}")
        return
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return False

    # Crear una copia de la imagen original para mantenerla inalterada
    imagen = imagen_original.copy()

    # Texto y configuración
    texto1 = f"{largo_value:.0f} mm"
    texto2 = f"{ancho_value:.0f} mm"
    texto3 = f"{largo2_value:.0f} mm"
    texto4 = f"R : {radio_value:.1f} mm"
    tamano = 22
    color = "black"

    # Preparación para dibujar sobre la copia
    dibujo = ImageDraw.Draw(imagen)

    # Carga de fuente
    try:
        fuente = ImageFont.truetype("arial.ttf", tamano)
    except:
        print("Usando fuente por defecto")
        fuente = ImageFont.load_default()

    # Cálculo de posiciones
    ancho_imagen, alto_imagen = imagen.size
    ancho_texto = dibujo.textlength(texto1, font=fuente)

    x1 = (ancho_imagen - ancho_texto) / 2
    y1 = alto_imagen / 5.7
    x2 = (ancho_imagen - ancho_texto) / 0.996
    y2 = alto_imagen / 2
    x3 = (ancho_imagen - ancho_texto) / 2
    y3 = alto_imagen / 3.85
    x4 = (ancho_imagen - ancho_texto) / 6.05
    y4 = alto_imagen / 2.05
    # Escritura del texto sobre la copia
    dibujo.text((x1, y1), texto1, fill=color, font=fuente)
    dibujo.text((x2, y2), texto2, fill=color, font=fuente)
    dibujo.text((x3, y3), texto3, fill=color, font=fuente)
    dibujo.text((x4, y4), texto4, fill= color ,font= fuente)

    # Definición de una ruta alternativa para guardar la imagen modificada
    directorio_guardado = r"C:\Users\Ulises\GUI_OMEGA\GUI\Dibujos"
    nombre_archivo = "TubularW_editada.jpg"  # Distinto del original
    ruta_completa = os.path.join(directorio_guardado, nombre_archivo)
    os.makedirs(directorio_guardado, exist_ok=True)

    try:
        imagen.save(ruta_completa)
        print(f"\nImagen modificada guardada en: {ruta_completa}")
        imagen.show()
    except Exception as e:
        print(f"\nError al guardar la imagen: {e}")

if __name__ == "__main__":
    largo_ejemplo = 100
    ancho_ejemplo = 80
    largo2_ejemplo = 70
    radio_ejemplo = 25.5
    agregar_texto_centradoW(largo_ejemplo, ancho_ejemplo, largo2_ejemplo, radio_ejemplo)
