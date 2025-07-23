from PIL import Image, ImageDraw, ImageFont
import os

def agregar_texto_centrado(largo_value, ancho_value):
    """
    Función que agrega texto a una copia de la imagen original usando los valores de largo y ancho.
    La imagen original no se modifica.
    
    Args:
        largo_value (str): Valor del largo desde la interfaz
        ancho_value (str): Valor del ancho desde la interfaz
    """
    # Ruta de la imagen original
    ruta_imagen_original = r"C:\Users\Ulises\GUI_OMEGA\GUI\Dibujos\TubularU.jpg"
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
    
    # Configuración del texto
    texto = f"{largo_value} mm"
    texto2 = f"{ancho_value} mm"
    tamano = 30
    color = "black"
    
    # Crear objeto para dibujar sobre la copia
    dibujo = ImageDraw.Draw(imagen)
    
    # Intentar cargar fuente
    try:
        fuente = ImageFont.truetype("arial.ttf", tamano)
    except:
        print("Usando fuente por defecto")
        fuente = ImageFont.load_default()
    
    # Calcular posición centrada para ambos textos
    ancho_imagen, alto_imagen = imagen.size
    ancho_texto1 = dibujo.textlength(texto, font=fuente)
    ancho_texto2 = dibujo.textlength(texto2, font=fuente)

    x1 = (ancho_imagen - ancho_texto1) / 2
    y1 = alto_imagen / 5
    x2 = (ancho_imagen - ancho_texto2) / 1.05
    y2 = alto_imagen / 2.1
    
    # Agregar texto sobre la copia
    dibujo.text((x1, y1), texto, fill=color, font=fuente)
    dibujo.text((x2, y2), texto2, fill=color, font=fuente)
    
    # Ruta de guardado para la imagen modificada
    directorio_guardado = r"C:\Users\Ulises\GUI_OMEGA\GUI\Dibujos"
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
    agregar_texto_centrado(largo_ejemplo, ancho_ejemplo)
