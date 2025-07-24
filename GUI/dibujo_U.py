from PIL import Image, ImageDraw, ImageFont
import os
import sys

def agregar_texto_centrado_u(largo_value,
                           ancho_value,
                           radio_interno):

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Cuando está empaquetado
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    ruta_imagen_original = os.path.join(base_path, "Dibujos", "TubularU.jpg")

    # Ruta de la imagen original
    try:
        # Abrir la imagen original
        imagen_original = Image.open(ruta_imagen_original)
    except FileNotFoundError:
        print(f"No se pudo encontrar la imagen en: {ruta_imagen_original}")
        return
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return

    # Crear una copia de la imagen para modificarla sin afectar la original
    imagen = imagen_original.copy()
    
    try:
        largo_value = float(largo_value)
        ancho_value = float(ancho_value)
        radio_interno = float(radio_interno)
        
    except ValueError:
        print("❌ Error: Los valores deben ser numéricos.")
        return
    
    # Configuración del texto
    texto = f"{largo_value} mm"
    texto2 = f"{ancho_value} mm"
    texto3 = f" R : {radio_interno:.1f} mm "
    tamano = 25
    color = "black"
    
    # Crear objeto para dibujar sobre la copia
    dibujo = ImageDraw.Draw(imagen)
    
    # Intentar cargar fuente
    try:
        fuente = ImageFont.truetype("arial.ttf", tamano)
    except:
        print("Usando fuente por defecto")
        fuente = ImageFont.load_default()
    
        # Cálculo de posiciones
    ancho_imagen, alto_imagen = imagen.size
    ancho_texto = dibujo.textlength(texto, font=fuente)

    
    # Calcular posición centrada para ambos textos
    x1 = (ancho_imagen - ancho_texto) / 2
    y1 = alto_imagen / 7
    x2 = (ancho_imagen - ancho_texto) / 0.996
    y2 = alto_imagen / 2
    x3 = (ancho_imagen - ancho_texto) / 1.3
    y3 = alto_imagen / 2.1
  
    # Escritura del texto sobre la copia
    dibujo.text((x1, y1), texto, fill=color, font=fuente)
    dibujo.text((x2, y2), texto2, fill=color, font=fuente)
    dibujo.text((x3, y3), texto3, fill=color, font=fuente)
    
    # Ruta de guardado para la imagen modificada
    directorio_guardado = os.path.join(base_path, "Dibujos")
    nombre_archivo = "TubularU_editada.jpg"  # <- Se cambia el nombre para no sobreescribir
    ruta_completa = os.path.join(directorio_guardado, nombre_archivo)
    
    # Crear directorio si no existe
    os.makedirs(directorio_guardado, exist_ok=True)

    # Guardar la imagen modificada
    try:
        imagen.save(ruta_completa)
        print(f"\nImagen modificada guardada correctamente en: {ruta_completa}")
        imagen.show()
    except Exception as e:
        print(f"\nError al guardar la imagen: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    largo_ejemplo = "150"
    ancho_ejemplo = "80"
    radio_interno = "11"
    agregar_texto_centrado_u(largo_ejemplo, ancho_ejemplo, radio_interno)
