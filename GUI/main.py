import customtkinter
import tkinter
from PIL import Image, ImageTk
import sys
import os
from tubularu import calcular_tubular_u
from datetime import datetime
from dibujo_U import agregar_texto_centrado_u
from dibujo_W import agregar_texto_centradoW
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Orden_final")))
from PDFU import generar_pdf_U  # o la función que definiste
from PDFW import generar_pdf_W
from tubularw import calcular_tubular_w


def load_image(image_path):
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None

# Imágenes para la tab de inicio
image_path_banda_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\banda.png"
pil_image_banda_inicio = load_image(image_path_banda_inicio)
if pil_image_banda_inicio:
    img_banda_inicio = customtkinter.CTkImage(light_image=pil_image_banda_inicio, dark_image=pil_image_banda_inicio, size=(100, 200))
else:
    img_banda_inicio = None

image_path_bancodeclima_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\bancodeclima chico.png"
pil_image_bancodeclima_inicio = load_image(image_path_bancodeclima_inicio)
if pil_image_bancodeclima_inicio:
    img_bancodeclima_inicio = customtkinter.CTkImage(light_image=pil_image_bancodeclima_inicio, dark_image=pil_image_bancodeclima_inicio, size=(100, 200))
else:
    img_bancodeclima_inicio = None

image_path_cartucho_inicio =r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\cartucho.png"
pil_image_cartucho_inicio = load_image(image_path_cartucho_inicio)
if pil_image_cartucho_inicio:
    img_cartucho_inicio = customtkinter.CTkImage(light_image=pil_image_cartucho_inicio, dark_image=pil_image_cartucho_inicio, size=(100, 200))
else:
    img_cartucho_inicio = None

image_path_tubular_inicio =r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\tubular.png"
pil_image_tubular_inicio = load_image(image_path_tubular_inicio)
if pil_image_tubular_inicio:
    img_tubular_inicio = customtkinter.CTkImage(light_image=pil_image_tubular_inicio, dark_image=pil_image_tubular_inicio, size=(100, 200))
else:
    img_tubular_inicio = None

image_path_termopar_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\termopar tipo j.png"
pil_image_termopar_inicio = load_image(image_path_termopar_inicio)
if pil_image_termopar_inicio:
    img_termopar_inicio = customtkinter.CTkImage(light_image=pil_image_termopar_inicio, dark_image=pil_image_termopar_inicio, size=(100, 200))
else:
    img_termopar_inicio = None
image_path_coiler_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\coiler.png"
pil_image_coiler_inicio = load_image(image_path_coiler_inicio)
if pil_image_coiler_inicio:
    img_coiler_inicio = customtkinter.CTkImage(light_image=pil_image_coiler_inicio, dark_image=pil_image_coiler_inicio, size=(100, 200))
else:
    img_coiler_inicio = None


# Imágenes para la tab de tubulares
image_path_tubular1_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\tubular brida mas pegada.jpg"
pil_image_tubular1_inicio = load_image(image_path_tubular1_inicio)
if pil_image_tubular1_inicio:
    img_tubular1_inicio = customtkinter.CTkImage(light_image=pil_image_tubular1_inicio, dark_image=pil_image_tubular1_inicio, size=(100, 200))
else:
    img_tubular1_inicio = None

image_path_tubular2_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\Tubular U.jpg"
pil_image_tubular2_inicio = load_image(image_path_tubular2_inicio)
if pil_image_tubular2_inicio:
    img_tubular2_inicio = customtkinter.CTkImage(light_image=pil_image_tubular2_inicio, dark_image=pil_image_tubular2_inicio, size=(100, 200))
else:
    img_tubular2_inicio = None

image_path_tubularW = r"C:\Users\Ulises\GUI_OMEGA\GUI\Dibujos\TUBULARW.jpg"
pil_image_tubular_W = load_image(image_path_tubularW)
if pil_image_tubular_W:
    img_tubular_w = customtkinter.CTkImage(light_image=pil_image_tubular_W, dark_image=pil_image_tubular_W, size=(100, 200))
else:
    img_tubular_w = None

image_path_tubular3_inicio = r"C:\Users\yffjy\OneDrive\Imágenes\Imagenes para interfaz\tubular brida.jpg"
pil_image_tubular3_inicio = load_image(image_path_tubular3_inicio)
if pil_image_tubular3_inicio:
    img_tubular3_inicio = customtkinter.CTkImage(light_image=pil_image_tubular3_inicio, dark_image=pil_image_tubular3_inicio, size=(100, 200))
else:
    img_tubular3_inicio = None

def run_power_calculator_app():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Interfaz para excel")
    app.geometry("1800x700")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    tabview = customtkinter.CTkTabview(app, width=750, height=550)
    tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Agregar tabs con "Inicio" como primera tab
    tabview.add("Inicio")
    tabview.add("Bandas")
    tabview.add("Tubulares")
    tabview.add("Tubular Recta")
    tabview.add("Tubular en U")
    tabview.add("Tubular en W")
    tabview.add("Tubular Brida")
    tabview.add("Cartuchos")
    tabview.add("Cartucho Alta Concentración")
    tabview.add("Cartucho Baja Concentración")
    tabview.add("Cartucho Titanio")
    tabview.add("Termopares")
    tabview.add("Bancos de Clima")
    tabview.add("Coilers")
    tabview.add("Bandas General Electric")
    tabview.add("Bandas cierre de perno")
    tabview.add("Bandas cierre de ceja")
    tabview.add("Bandas medias cañas")
    tabview.set("Inicio")

    global img_for_textbox, img_tubular_recta, img_tubular_brida 

    # Cargar imagen para Bandas
    image_path = (r"imagenbrida.jpg") 
    pil_image = load_image(image_path)
    
    # Cargar imagen para Tubular recta
    image_path_tubular_recta = (r"C:\Users\yffjy\OneDrive\Imágenes\imagenbrida\tubular recta.jpg") 
    pil_image_tubular_recta = load_image(image_path_tubular_recta)
    
    # Cargar imagen para Tubular brida
    image_path_tubular_brida = (r"C:\Users\yffjy\OneDrive\Imágenes\imagenbrida\tubularbrida.jpg") 
    pil_image_tubular_brida = load_image(image_path_tubular_brida)

    # Procesar imagen para Bandas
    if pil_image:
        max_width = 1250
        width, height = pil_image.size
        if width > max_width:
            new_height = int(height * (max_width / width))
            pil_image = pil_image.resize((max_width, new_height), Image.Resampling.LANCZOS)
        img_for_textbox = customtkinter.CTkImage(light_image=pil_image, dark_image=pil_image, size=pil_image.size)
    else:
        print("No se pudo cargar la imagen de Bandas.")
        img_for_textbox = None

    # Procesar imagen para Tubular recta
    if pil_image_tubular_recta:
        max_width = 1250
        width, height = pil_image_tubular_recta.size
        if width > max_width:
            new_height = int(height * (max_width / width))
            pil_image_tubular_recta = pil_image_tubular_recta.resize((max_width, new_height), Image.Resampling.LANCZOS)
        img_tubular_recta = customtkinter.CTkImage(light_image=pil_image_tubular_recta, dark_image=pil_image_tubular_recta, size=pil_image_tubular_recta.size)
    else:
        print("No se pudo cargar la imagen de Tubular recta.")
        img_tubular_recta = None

    # Procesar imagen para Tubular brida
    if pil_image_tubular_brida:
        max_width = 1250
        width, height = pil_image_tubular_brida.size
        if width > max_width:
            new_height = int(height * (max_width / width))
            pil_image_tubular_brida = pil_image_tubular_brida.resize((max_width, new_height), Image.Resampling.LANCZOS)
        img_tubular_brida = customtkinter.CTkImage(light_image=pil_image_tubular_brida, dark_image=pil_image_tubular_brida, size=pil_image_tubular_brida.size)
    else:
        print("No se pudo cargar la imagen de Tubular brida.")
        img_tubular_brida = None

    def create_home_tab():
        """Crear la tab de inicio con botones para navegar a otras tabs"""
        home_frame = tabview.tab("Inicio")
        
        # Crear un scrollable frame para acomodar todas las opciones
        scrollable_frame = customtkinter.CTkScrollableFrame(home_frame, width=1700, height=600)
        scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configurar el grid del scrollable frame
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)
        scrollable_frame.grid_columnconfigure(2, weight=1)
        
        # Título
        title_label = customtkinter.CTkLabel(
            scrollable_frame, 
            text="Inicio", 
            font=("Arial", 24, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=30, sticky="ew")
        
        # Función para cambiar a una tab específica
        def go_to_tab(tab_name):
            tabview.set(tab_name)
        
        # Función para cargar imagen de preview (placeholder)
        def create_image_placeholder(parent, width=100, height=200):
            """Crear un placeholder para imagen de 100x200 píxeles"""
            placeholder_frame = customtkinter.CTkFrame(parent, width=width, height=height)
            placeholder_frame.grid_propagate(False)  # Mantener el tamaño fijo
            
            placeholder_label = customtkinter.CTkLabel(
                placeholder_frame,
                text="Imagen\n100x200",
                font=("Arial", 12),
                text_color="gray"
            )
            placeholder_label.place(relx=0.5, rely=0.5, anchor="center")
            
            return placeholder_frame
        
        # Opciones con sus descripciones
        options = [
            ("Bandas", ""),
            ("Tubulares", ""),
            ("Cartuchos", ""),
            ("Termopares", ""),
            ("Bancos de Clima", ""),
            ("Coilers", "")
        ]
        
        # Crear las opciones en grid de 3 columnas
        for i, (tab_name, description) in enumerate(options):
            row = (i // 3) + 1  # Tres columnas por fila
            col = i % 3

            # Frame principal para cada opción
            main_option_frame = customtkinter.CTkFrame(scrollable_frame)
            main_option_frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
            main_option_frame.grid_columnconfigure(0, weight=1)
            main_option_frame.grid_rowconfigure(1, weight=1)

            # Título de la opción
            title_frame = customtkinter.CTkFrame(main_option_frame)
            title_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

            option_title = customtkinter.CTkLabel(
                title_frame,
                text=tab_name,
                font=("Arial", 16, "bold")
            )
            option_title.grid(row=0, column=0, pady=10)

            # Imagen real para Bandas, placeholder para otros
            if tab_name == "Bandas" and img_banda_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_banda_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            elif tab_name == "Bancos de Clima" and img_bancodeclima_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_bancodeclima_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            elif tab_name == "Cartuchos" and img_cartucho_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_cartucho_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            elif tab_name == "Tubulares" and img_tubular_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_tubular_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            elif tab_name == "Termopares" and img_termopar_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_termopar_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            elif tab_name == "Coilers" and img_coiler_inicio:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img_coiler_inicio, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            else:
                image_placeholder = create_image_placeholder(main_option_frame)
                image_placeholder.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            # Frame para descripción y botón
            bottom_frame = customtkinter.CTkFrame(main_option_frame)
            bottom_frame.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")
            bottom_frame.grid_columnconfigure(0, weight=1)

            # Descripción
            desc_label = customtkinter.CTkLabel(
                bottom_frame,
                text=description,
                font=("Arial", 11),
                text_color="gray",
                wraplength=280
            )
            desc_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

            # Botón para acceder
            access_button = customtkinter.CTkButton(
                bottom_frame,
                text=f"Ir a {tab_name}",
                font=("Arial", 12, "bold"),
                height=35,
                corner_radius=8,
                command=lambda t=tab_name: go_to_tab(t)
            )
            access_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")
        
        # Configurar peso de las filas para mejor distribución
        for i in range(3):  # 2 filas de opciones + título
            scrollable_frame.grid_rowconfigure(i, weight=1)
        
        # Configurar el frame principal para expandirse
        home_frame.grid_columnconfigure(0, weight=1)
        home_frame.grid_rowconfigure(0, weight=1)

    def create_tubulares_tab():
        """Crear la tab de tubulares con opciones específicas"""
        tubulares_frame = tabview.tab("Tubulares")
        
        # Crear un scrollable frame para acomodar todas las opciones
        scrollable_frame = customtkinter.CTkScrollableFrame(tubulares_frame, width=1700, height=600)
        scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configurar el grid del scrollable frame
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)
        scrollable_frame.grid_columnconfigure(2, weight=1)
        scrollable_frame.grid_columnconfigure(3, weight=1)
        
        # Botón para regresar al inicio
        back_button = customtkinter.CTkButton(
            scrollable_frame,
            text="← Regresar al Inicio",
            command=lambda: tabview.set("Inicio"),
            width=150,
            height=30,
            corner_radius=5
        )
        back_button.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")
        
        # Título
        title_label = customtkinter.CTkLabel(
            scrollable_frame, 
            text="Tubulares - Seleccione el tipo de tubular", 
            font=("Arial", 24, "bold")
        )
        title_label.grid(row=1, column=0, columnspan=4, pady=30, sticky="ew")
        
        # Función para cambiar a una tab específica
        def go_to_tab(tab_name):
            tabview.set(tab_name)
        
        # Función para cargar imagen de preview (placeholder)
        def create_image_placeholder(parent, width=100, height=200):
            """Crear un placeholder para imagen de 100x200 píxeles"""
            placeholder_frame = customtkinter.CTkFrame(parent, width=width, height=height)
            placeholder_frame.grid_propagate(False)  # Mantener el tamaño fijo
            
            placeholder_label = customtkinter.CTkLabel(
                placeholder_frame,
                text="Imagen\n100x200",
                font=("Arial", 12),
                text_color="gray"
            )
            placeholder_label.place(relx=0.5, rely=0.5, anchor="center")
            
            return placeholder_frame
        
        # Opciones específicas de tubulares con sus imágenes correspondientes
        tubular_options = [
            ("Tubular Recta", "Resistencias tubulares de forma recta para calentamiento lineal", img_tubular1_inicio),
            ("Tubular en U", "Resistencias tubulares en forma de U para espacios reducidos", img_tubular2_inicio),
            ("Tubular en W", "Resistencias tubulares en forma de W para mayor superficie de contacto", img_tubular3_inicio),
            ("Tubular Brida", "Resistencias tubulares con brida para montaje en tanques", None)
        ]
        
        # Crear las opciones en grid de 4 columnas
        for i, (tab_name, description, img) in enumerate(tubular_options):
            row = 2  # Fila 2 (después del título)
            col = i % 4
            
            # Frame principal para cada opción
            main_option_frame = customtkinter.CTkFrame(scrollable_frame)
            main_option_frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
            main_option_frame.grid_columnconfigure(0, weight=1)
            main_option_frame.grid_rowconfigure(1, weight=1)
            
            # Título de la opción
            title_frame = customtkinter.CTkFrame(main_option_frame)
            title_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
            
            option_title = customtkinter.CTkLabel(
                title_frame,
                text=tab_name,
                font=("Arial", 16, "bold")
            )
            option_title.grid(row=0, column=0, pady=10)
            
            # Frame para imagen (100x200 píxeles)
            if img:
                image_label = customtkinter.CTkLabel(main_option_frame, image=img, text="")
                image_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            else:
                image_placeholder = create_image_placeholder(main_option_frame)
                image_placeholder.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            
            # Frame para descripción y botón
            bottom_frame = customtkinter.CTkFrame(main_option_frame)
            bottom_frame.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")
            bottom_frame.grid_columnconfigure(0, weight=1)
            
            # Descripción
            desc_label = customtkinter.CTkLabel(
                bottom_frame,
                text=description,
                font=("Arial", 11),
                text_color="gray",
                wraplength=280
            )
            desc_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
            
            # Botón para acceder
            access_button = customtkinter.CTkButton(
                bottom_frame,
                text=f"Acceder a {tab_name}",
                font=("Arial", 12, "bold"),
                height=35,
                corner_radius=8,
                command=lambda t=tab_name: go_to_tab(t)
            )
            access_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")
        
        # Configurar peso de las filas para mejor distribución
        for i in range(3):  # 2 filas de opciones + título
            scrollable_frame.grid_rowconfigure(i, weight=1)
        
        # Configurar el frame principal para expandirse
        tubulares_frame.grid_columnconfigure(0, weight=1)
        tubulares_frame.grid_rowconfigure(0, weight=1)

    def create_cartuchos_tab():
        """Crear la tab de cartuchos con opciones específicas"""
        cartuchos_frame = tabview.tab("Cartuchos")
        
        # Crear un scrollable frame para acomodar todas las opciones
        scrollable_frame = customtkinter.CTkScrollableFrame(cartuchos_frame, width=1700, height=600)
        scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configurar el grid del scrollable frame
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)
        scrollable_frame.grid_columnconfigure(2, weight=1)
        
        # Botón para regresar al inicio
        back_button = customtkinter.CTkButton(
            scrollable_frame,
            text="← Regresar al Inicio",
            command=lambda: tabview.set("Inicio"),
            width=150,
            height=30,
            corner_radius=5
        )
        back_button.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")
        
        # Título
        title_label = customtkinter.CTkLabel(
            scrollable_frame, 
            text="Cartuchos - Seleccione el tipo de cartucho", 
            font=("Arial", 24, "bold")
        )
        title_label.grid(row=1, column=0, columnspan=3, pady=30, sticky="ew")
        
        # Función para cambiar a una tab específica
        def go_to_tab(tab_name):
            tabview.set(tab_name)
        
        # Función para cargar imagen de preview (placeholder)
        def create_image_placeholder(parent, width=100, height=200):
            """Crear un placeholder para imagen de 100x200"""
            placeholder_frame = customtkinter.CTkFrame(parent, width=width, height=height)
            placeholder_frame.grid_propagate(False)  # Mantener el tamaño fijo
            
            placeholder_label = customtkinter.CTkLabel(
                placeholder_frame,
                text="Imagen\n100x200",
                font=("Arial", 12),
                text_color="gray"
            )
            placeholder_label.place(relx=0.5, rely=0.5, anchor="center")
            
            return placeholder_frame
        
        # Opciones específicas de cartuchos
        cartucho_options = [
            ("Cartucho Alta Concentración", "Cartuchos de alta concentración de potencia para aplicaciones industriales"),
            ("Cartucho Baja Concentración", "Cartuchos de baja concentración para aplicaciones de precisión"),
            ("Cartucho Titanio", "Cartuchos especiales de titanio para ambientes corrosivos")
        ]
        
        # Crear las opciones en grid de 3 columnas
        for i, (tab_name, description) in enumerate(cartucho_options):
            row = 2  # Fila 2 (después del título)
            col = i % 3
            
            # Frame principal para cada opción
            main_option_frame = customtkinter.CTkFrame(scrollable_frame)
            main_option_frame.grid(row=row, column=col, padx=20, pady=20, sticky="nsew")
            main_option_frame.grid_columnconfigure(0, weight=1)
            main_option_frame.grid_rowconfigure(1, weight=1)
            
            # Título de la opción
            title_frame = customtkinter.CTkFrame(main_option_frame)
            title_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
            
            option_title = customtkinter.CTkLabel(
                title_frame,
                text=tab_name,
                font=("Arial", 16, "bold")
            )
            option_title.grid(row=0, column=0, pady=10)
            
            # Frame para imagen (300x400 píxeles)
            image_placeholder = create_image_placeholder(main_option_frame)
            image_placeholder.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
            
            # Frame para descripción y botón
            bottom_frame = customtkinter.CTkFrame(main_option_frame)
            bottom_frame.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")
            bottom_frame.grid_columnconfigure(0, weight=1)
            
            # Descripción
            desc_label = customtkinter.CTkLabel(
                bottom_frame,
                text=description,
                font=("Arial", 11),
                text_color="gray",
                wraplength=280
            )
            desc_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
            
            # Botón para acceder
            access_button = customtkinter.CTkButton(
                bottom_frame,
                text=f"Ir a {tab_name}",
                font=("Arial", 12, "bold"),
                height=35,
                corner_radius=8,
                command=lambda t=tab_name: go_to_tab(t)
            )
            access_button.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="ew")
        
        # Configurar peso de las filas para mejor distribución
        for i in range(3):  # 2 filas de opciones + título
            scrollable_frame.grid_rowconfigure(i, weight=1)
        
        # Configurar el frame principal para expandirse
        cartuchos_frame.grid_columnconfigure(0, weight=1)
        cartuchos_frame.grid_rowconfigure(0, weight=1)

    def create_calculator_ui_in_frame(parent_frame, tab_name):
        parent_frame.grid_columnconfigure(0, weight=0)
        parent_frame.grid_columnconfigure(1, weight=0)
        parent_frame.grid_columnconfigure(2, weight=2)  # Más espacio para la imagen
        parent_frame.grid_columnconfigure(3, weight=1)  # Espacio para info
        parent_frame.grid_rowconfigure(0, weight=1)
        parent_frame.grid_rowconfigure(1, weight=1)
        parent_frame.grid_rowconfigure(2, weight=1)
        parent_frame.grid_rowconfigure(3, weight=0)

        entries = {}

        # Definir campos según la tab
        if tab_name == "Bandas":
            labels = ["Volts", "watts", "Amperes"]
            back_tab = "Inicio"
        elif tab_name == "Tubular Recta":
            labels = ["Voltaje", "Potencia", "Longitud", "Diámetro"]
            back_tab = "Tubulares"
        elif tab_name == "Tubular en U":
            labels = ["Cliente","Numero_de_Orden","unidades","Elementos_por_unidad","Volts", "Watts", "Largo", "Ancho", "Tornillo"]
            back_tab = "Tubulares"
        elif tab_name == "Tubular en W":
            labels = ["Cliente","Numero_de_Orden","unidades","Elementos_por_unidad","Volts", "Watts", "Largo", "Largo2", "Ancho", "Tornillo"]
            back_tab = "Tubulares"
        elif tab_name == "Tubular Brida":
            labels = ["Voltaje", "Potencia", "Longitud", "Diámetro Brida"]
            back_tab = "Tubulares"
        elif tab_name == "Cartucho Alta Concentración":
            labels = ["Voltaje", "Potencia Alta", "Diámetro", "Longitud"]
            back_tab = "Cartuchos"
        elif tab_name == "Cartucho Baja Concentración":
            labels = ["Voltaje", "Potencia Baja", "Diámetro", "Longitud"]
            back_tab = "Cartuchos"
        elif tab_name == "Cartucho Titanio":
            labels = ["Voltaje", "Potencia", "Diámetro", "Material Titanio"]
            back_tab = "Cartuchos"
        elif tab_name == "Termopares":
            labels = ["Tipo", "Longitud Bulbo", "Extensión"]
            back_tab = "Inicio"
        elif tab_name == "Bancos de Clima":
            labels = ["Temperatura", "Humedad", "Presión"]
            back_tab = "Inicio"
        elif tab_name == "Coilers":
            labels = ["Voltaje", "Potencia", "Diámetro Serpentín"]
            back_tab = "Inicio"
        elif tab_name == "Bandas General Electric":
            labels = ["Voltaje", "Potencia", "Ancho Banda", "Longitud Banda"]
            back_tab = "Inicio"
        elif tab_name == "Bandas cierre de perno":
            labels = ["Voltaje", "Potencia", "Ancho Banda", "Longitud Banda"]
            back_tab = "Inicio"
        elif tab_name == "Bandas cierre de ceja":
            labels = ["Voltaje", "Potencia", "Ancho Banda", "Longitud Banda"]
            back_tab = "Inicio"
        elif tab_name == "Bandas medias cañas":
            labels = ["Voltaje", "Potencia", "Ancho Banda", "Longitud Banda"]
            back_tab = "Inicio" 
        else:
            labels = ["Campo 1", "Campo 2", "Campo 3"]
            back_tab = "Inicio"
        
       
        # Botón para regresar
        back_button = customtkinter.CTkButton(
            parent_frame,
            text=f"← Regresar a {back_tab}",
            command=lambda: tabview.set(back_tab),
            width=150,
            height=30,
            corner_radius=5
        )
        back_button.grid(row=0, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="w")

        # Add radio buttons specifically for "Tubular en U" tab
        if tab_name == "Tubular en U" or tab_name == "Tubular en W":
            diameter_var = tkinter.StringVar(value="") # Variable to hold the selected diameter

            diameter_label = customtkinter.CTkLabel(parent_frame, text="Diámetro:", font=("Arial", 14, "bold"))
            diameter_label.grid(row=1, column=0, padx=(20, 10), pady=2, sticky="w")

            radio_3_8 = customtkinter.CTkRadioButton(parent_frame, text="Diámetro 3/8",
                                                     variable=diameter_var, value="3/8")
            radio_3_8.grid(row=1, column=1, padx=(0, 20), pady=2, sticky="w")

            radio_1_2 = customtkinter.CTkRadioButton(parent_frame, text="Diámetro 1/2",
                                                     variable=diameter_var, value="1/2")
            radio_1_2.grid(row=2, column=1, padx=(0, 20), pady=2, sticky="w")
            
            # Adjust the starting row for labels and entries if radio buttons are added
            start_row_for_entries = 3 
        else:
            start_row_for_entries = 1

        # Crear labels y entries lado a lado (empezar desde adjusted row)
        for i, label_text in enumerate(labels):
            row_pos = i + start_row_for_entries
            
            # Label en la columna 0
            label = customtkinter.CTkLabel(parent_frame, text=f"{label_text}:", font=("Arial", 14, "bold"))
            label.grid(row=row_pos, column=0, padx=(20, 10), pady=2, sticky="w")  # Reducir pady de 5 a 2

            # Entry en la columna 1
            entry = customtkinter.CTkEntry(parent_frame, placeholder_text=f"Ingrese {label_text}", width=200)
            entry.grid(row=row_pos, column=1, padx=(0, 20), pady=2, sticky="w")  # Reducir pady de 5 a 2
            entries[label_text] = entry

        # Frame para la imagen con botones superpuestos
        image_frame = tkinter.Frame(parent_frame, bg="white")
        # Adjust rowspan based on whether radio buttons are present
        image_rowspan = 3 if tab_name != "Tubular en U" else (3 + (len(labels) - (start_row_for_entries -1)) + 1) # This needs to be dynamic, 
                                                                                        # ensuring image_frame spans enough rows
        
        # Calculate the correct rowspan for image_frame
        # The number of rows for entries + 1 (for the "Mostrar Valores" button row)
        if tab_name == "Tubular en U":
            # 1 for back button, 2 for radio buttons, then labels
            actual_content_rows = 1 + 2 + len(labels) + 1 # back_button, diameter_label, radio_3_8, radio_1_2, labels, button_display
            image_frame_row = 1 # starting row for image
            image_rowspan = actual_content_rows - image_frame_row # span from image_row to the last content row
        else:
            actual_content_rows = 1 + len(labels) + 1 # back_button, labels, button_display
            image_frame_row = 1
            image_rowspan = actual_content_rows - image_frame_row

        image_frame.grid(row=image_frame_row, column=2, rowspan=image_rowspan, padx=(10, 0), pady=20, sticky="nsew")
        
        # Canvas para mostrar la imagen y colocar botones encima
        canvas = tkinter.Canvas(image_frame, bg="white")
        canvas.pack(fill="both", expand=True)
        
        # Scrollbars para el canvas
        v_scrollbar = tkinter.Scrollbar(image_frame, orient="vertical", command=canvas.yview)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar = tkinter.Scrollbar(image_frame, orient="horizontal", command=canvas.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Frame interno para contener la imagen y los botones
        inner_frame = tkinter.Frame(canvas, bg="white")
        canvas_frame = canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        # Mostrar la imagen
        image_label = None
        interactive_buttons = []
        
        # Determinar qué imagen usar según la pestaña
        current_image = None
        if tab_name == "Bandas" and img_for_textbox:
            current_image = img_for_textbox
        elif tab_name in ["Tubular Recta", "Tubular en U"] and img_tubular_recta:
            current_image = img_tubular_recta
        elif tab_name == "Tubular en W" and pil_image_tubular_W: 
            current_image = img_tubular_w
        elif tab_name == "Tubular Brida" and img_tubular_brida:
            current_image = img_tubular_brida
        
        if current_image and tab_name in ["Bandas", "Tubular Recta", "Tubular en U", "Tubular en W", "Tubular Brida"]:
            pil_image_to_embed = current_image._light_image or current_image._dark_image
            tk_image_to_embed = ImageTk.PhotoImage(pil_image_to_embed)
            
            # Label para mostrar la imagen
            image_label = tkinter.Label(inner_frame, image=tk_image_to_embed, bg="white")
            image_label.image = tk_image_to_embed  # Mantener referencia
            image_label.place(x=0, y=0)
            
            # Función para crear botones interactivos sobre la imagen
            def create_interactive_button(x, y, text="Medidas"):
                button = customtkinter.CTkButton(
                    inner_frame,
                    text=text,
                    width=60,
                    height=25,
                    font=("Arial", 10),
                    corner_radius=5,
                    command=lambda: open_input_dialog(text, x, y)
                )
                button.place(x=x, y=y)
                interactive_buttons.append(button)
                return button
            
            # Función para abrir diálogo de entrada de texto
            def open_input_dialog(button_text, x, y):
                dialog = customtkinter.CTkInputDialog(text=f"Ingrese texto para {button_text} (x:{x}, y:{y}):", title="Entrada de Texto")
                user_input = dialog.get_input()
                if user_input:
                    # Actualizar el texto del botón
                    for btn in interactive_buttons:
                        if btn.winfo_x() == x and btn.winfo_y() == y:
                            btn.configure(text=user_input[:8])  # Limitar texto a 8 caracteres
                            break
                    # Mostrar en el área de texto
                    show_point_info(button_text, x, y, user_input)
            
            # Función para mostrar información del punto
            def show_point_info(button_text, x, y, text):
                text_widget.config(state="normal")
                text_widget.insert("end", f"\n{button_text} (x:{x}, y:{y}): {text}")
                text_widget.config(state="disabled")
           
            # Crear botones según la pestaña
            if tab_name == "Bandas":
                create_interactive_button(170, 310, "Tamaño 1")
                create_interactive_button(50, 150, "Tamaño 2")
                create_interactive_button(140, 150, "Tamaño 3")
                create_interactive_button(400, 20, "Tamaño 4")
                create_interactive_button(775, 170, "Tamaño 5")
            elif tab_name == "Tubulares": # This tab "Tubulares" is a menu, not a calculation tab, consider removing interactive buttons here
                create_interactive_button(100, 50, "Medida 1") 
                create_interactive_button(300, 100, "Medida 2")
                create_interactive_button(500, 150, "Medida 3")
                create_interactive_button(200, 200, "Medida 4")
                create_interactive_button(400, 250, "Medida 5")
            elif tab_name == "Tubular en U": # Example interactive buttons for Tubular en U
                create_interactive_button(150, 100, "Curvatura")
                create_interactive_button(50, 250, "Longitud")


            inner_frame.configure(width=pil_image_to_embed.width, height=pil_image_to_embed.height)
            canvas.configure(scrollregion=canvas.bbox("all"))
        else:
            # Si no hay imagen, mostrar texto
            no_image_label = tkinter.Label(inner_frame, text=f"Imagen no disponible para {tab_name}", bg="white")
            no_image_label.pack(pady=50)
        
        # Función para actualizar el scroll region
        def configure_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        inner_frame.bind("<Configure>", configure_scroll_region)
        
        # Texto widget para mostrar información adicional
        info_frame = tkinter.Frame(parent_frame)
        info_frame.grid(row=image_frame_row, column=3, rowspan=image_rowspan, padx=(10, 20), pady=20, sticky="nsew") # Adjust rowspan
        
        text_widget = tkinter.Text(info_frame, width=30, height=12, wrap="word", font=("Arial", 10))
        text_widget.pack(fill="both", expand=True)
        
        text_widget.insert("1.0", f"Información - {tab_name}:\n" + "="*30 + "\n")
        text_widget.config(state="disabled")

        def update_result_display_for_this_instance():
            global watts_value
            text_widget.config(state="normal")
            text_widget.delete("1.0", "end")
            
            text_widget.insert("1.0", f"Información - {tab_name}:\n" + "="*30 + "\n")
            
            output_text = "\n".join([f"{key}: {entry.get()}" for key, entry in entries.items()])
            
            # Add selected diameter for "Tubular en U"
            if tab_name == "Tubular en U":
                selected_diameter = diameter_var.get()
                if selected_diameter:
                    output_text += f"\nDiámetro Seleccionado: {selected_diameter}"
                
                # Capturar los valores de Voltaje y Potencia en variables
                cliente = entries["Cliente"].get()
                N_orden = entries["Numero_de_Orden"].get()
                unidades = entries["unidades"].get()
                elementos_por_unidad = entries["Elementos_por_unidad"].get()
                volts_value = entries["Volts"].get()
                watts_value = entries["Watts"].get()
                largo_value = entries["Largo"].get()
                ancho_value = entries["Ancho"].get()
                tornillos_value = entries["Tornillo"].get()

                
                # # Aquí puedes usar volts_value y watts_value para tus cálculos o procesamiento
                # # Por ejemplo, imprimirlos en la consola o en el text_widget
                # output_text += f"\n\nValores capturados para cálculos:"
                # output_text += f"\nVoltaje: {volts_value}"
                # output_text += f"\nPotencia: {watts_value}"
                
                # Ejemplo de uso: convertir a float (manejar errores si no son números)
                try:
                    volts = float(volts_value)
                    watts = float(watts_value)
                    largo = float(largo_value)
                    ancho = float(ancho_value)
                    tornillos = float(tornillos_value)
                    elementos_por_unidad = float(elementos_por_unidad)
                    unidades = float(unidades)
                    piezas = elementos_por_unidad*unidades
                    
                    
                    results = calcular_tubular_u(
                        diam_tubo=selected_diameter,
                        watts=watts,
                        volts=volts,
                        largo=largo,
                        ancho=ancho,
                        tornillos=70
                    )
                    # output_text += f"\n\nVoltaje (float): {volts}"
                    # output_text += f"\nPotencia (float): {watts}"
             #   except ValueError:
              #      output_text += "\nError: Voltaje o Potencia no son números válidos."
                    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
                    datos_pdf = {
                        "cliente": str(cliente),
                        "orden": str(N_orden),
                        "unidades": str(unidades),
                        "elementos_por_unidad": str(elementos_por_unidad),
                        "fecha": fecha_hoy,
                        "piezas": str(piezas),
                        "entrega": "25/07/2025",
                        "watts": watts_value,
                        "volts": volts_value,
                        "Material": "Acero Inoxidable",
                        "Diametro": selected_diameter,
                    }

                    if results["valido"]:
                        print("✅ Calibre válido:", results["calibre"])
                        print("📏 Separación:", results["separacion"])
                        
                        # Agregar imagen con medidas (solo si es válido)
                        radio_interno = results.get("radio_interno", 0)
                        print(f"🖼️ Generando imagen con valores: Largo={largo}, Ancho={ancho}, Radio={radio_interno}")

                        agregar_texto_centrado_u(largo, 
                                                ancho,  
                                                radio_interno)
                        
                        # Actualizar datos_pdf con resultados válidos
                        datos_pdf.update({
                            "Ampers": f"{results['amps']:.2f}",
                            "ohms": f"{results['ohms']:.2f}",
                            "ohms_tol_ab" : f"{results['ohms_tol_ab']:.2f}",
                            "ohms_tol_ar" : f"{results['ohms_tol_ar']:.2f}",
                            "largo": f"{results['largo_tubo']:.0f}",
                            "calibre": str(results["calibre"]),
                            "Husillo": str(results["husillo"]),
                            "bobina a": str(results["bobina_ohms"]),
                            "Long Bobina": f"{results['bobina_sin_estirar']:.2f}",
                            "Cortar a": f"{results['cortar_tubo']:.0f}",
                        })
                    else:
                        print("❌ No se encontró calibre válido")
                        print("➡️ Mejor candidato:", results["mejor_candidato"])
                        
                        # Actualizar datos_pdf con valores por defecto/error
                        datos_pdf.update({
                            "Ampers": f"{results['amps']:.2f}",
                            "ohms": f"{results['ohms']:.2f}",
                            "largo": "No calculado",
                            "calibre": "No válido",
                            "Husillo": "3/8",
                            "bobina a": "21",
                            "Long Bobina": "no valido",
                            "Cortar a": "no valido",
                        })
                    generar_pdf_U(datos_pdf)

                except ValueError:
                    output_text += "\nError: Los valores ingresados no son números válidos."


            elif tab_name == "Tubular en W":
                selected_diameter = diameter_var.get()
                if selected_diameter:
                    output_text += f"\nDiámetro Seleccionado: {selected_diameter}"
                
                # Capturar los valores de la interfaz
                cliente = entries["Cliente"].get()
                N_orden = entries["Numero_de_Orden"].get()
                unidades = entries["unidades"].get()
                elementos_por_unidad = entries["Elementos_por_unidad"].get()
                volts_value = entries["Volts"].get()
                watts_value = entries["Watts"].get()
                largo_value = entries["Largo"].get()
                largo2_value = entries["Largo2"].get()
                ancho_value = entries["Ancho"].get()
                tornillos_value = entries["Tornillo"].get()

                # output_text += f"\n\nValores capturados para cálculos:"
                # output_text += f"\nVoltaje: {volts_value}"
                # output_text += f"\nPotencia: {watts_value}"
                # output_text += f'\nLargo2 : {largo2_value}'
                
                try:
                    # Convertir valores a float
                    volts = float(volts_value)
                    watts = float(watts_value)
                    largo = float(largo_value)
                    largo2 = float(largo2_value)
                    ancho = float(ancho_value)
                    tornillos = float(tornillos_value)
                    elementos_por_unidad = float(elementos_por_unidad)
                    unidades = float(unidades)
                    piezas = elementos_por_unidad*unidades
                    
                    # Llamar a la función de cálculo 
                    results = calcular_tubular_w(
                        diam_tubo=selected_diameter,  
                        watts=watts,                 
                        volts=volts,                 
                        largo_tub=largo,             
                        largo2=largo2,               
                        ancho=ancho,                 
                        tornillos=tornillos,
                    )

                    # Configurar valores comunes para el PDF
                    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
                    datos_pdf = {
                        "cliente": str(cliente),
                        "orden": str(N_orden),
                        "unidades": str(unidades),
                        "elementos_por_unidad": str(elementos_por_unidad),
                        "fecha": fecha_hoy,
                        "piezas": str(piezas),
                        "entrega": "25/07/2025",
                        "watts": watts_value,
                        "volts": volts_value,
                        "Material": "Acero Inoxidable",
                        "Diametro": selected_diameter,
                    }

                    if results["valido"]:
                        print("✅ Calibre válido:", results["calibre"])
                        print("📏 Separación:", results["separacion"])
                        
                        # Agregar imagen con medidas (solo si es válido)
                        radio_interno = results.get("radio_interno", 0)
                        print(f"🖼️ Generando imagen con valores: Largo={largo}, Ancho={ancho}, Largo2={largo2}, Radio={radio_interno}")

                        agregar_texto_centradoW(largo, 
                                                ancho, 
                                                largo2, 
                                                radio_interno)
                        
                        # Actualizar datos_pdf con resultados válidos
                        datos_pdf.update({
                            "Ampers": f"{results['amps']:.2f}",
                            "ohms": f"{results['ohms']:.2f}",
                            "ohms_tol_ab" : f"{results['ohms_tol_ab']:.2f}",
                            "ohms_tol_ar" : f"{results['ohms_tol_ar']:.2f}",                            
                            "largo": f"{results['largo_tubo']:.0f}",
                            "calibre": str(results["calibre"]),
                            "Husillo": str(results["husillo"]),
                            "bobina a": str(results["bobina_ohms"]),
                            "Long Bobina": f"{results['bobina_sin_estirar']:.2f}",
                            "Cortar a": f"{results['cortar_tubo']:.0f}",
                        })
                    else:
                        print("❌ No se encontró calibre válido")
                        print("➡️ Mejor candidato:", results["mejor_candidato"])
                        
                        # Actualizar datos_pdf con valores por defecto/error
                        datos_pdf.update({
                            "Ampers": f"{results['amps']:.2f}",
                            "ohms": f"{results['ohms']:.2f}",
                            "largo": "No calculado",
                            "calibre": "No válido",
                            "Husillo": "3/8",
                            "bobina a": "21",
                            "Long Bobina": "no valido",
                            "Cortar a": "no valido",
                        })

                    # Generar PDF (con o sin imagen según results["valido"])
                    generar_pdf_W(datos_pdf)

                except ValueError:
                    output_text += "\nError: Los valores ingresados no son números válidos."



            text_widget.insert("end", f"\nValores ingresados:\n{output_text}\n")
            text_widget.insert("end", "\nHaga clic en los botones sobre la imagen para agregar información específica de cada punto.\n")

            text_widget.config(state="disabled")

        # Botón en la fila 4, columna 0, que ocupe 2 columnas. Adjust row based on labels
        button_display_row = start_row_for_entries + len(labels)
        button_display = customtkinter.CTkButton(
            master=parent_frame,
            text="Mostrar Valores",
            command=update_result_display_for_this_instance,
            width=150,
            height=40,
            corner_radius=10
        )
        button_display.grid(row=button_display_row, column=0, columnspan=2, padx=20, pady=20, sticky="w") # Place below entries

    # Crear la tab de inicio primerowww
    create_home_tab()
    
    # Crear la nueva tab de cartuchos
    create_cartuchos_tab()
    
    create_tubulares_tab()
    # Crear todas las tabs
    create_calculator_ui_in_frame(tabview.tab("Bandas"), tab_name="Bandas")
    create_calculator_ui_in_frame(tabview.tab("Tubulares"), tab_name="Tubulares")
    create_calculator_ui_in_frame(tabview.tab("Tubular Recta"), tab_name="Tubular Recta")
    create_calculator_ui_in_frame(tabview.tab("Tubular en U"), tab_name="Tubular en U")
    create_calculator_ui_in_frame(tabview.tab("Tubular en W"), tab_name="Tubular en W")
    create_calculator_ui_in_frame(tabview.tab("Tubular Brida"), tab_name="Tubular Brida")
    create_calculator_ui_in_frame(tabview.tab("Cartucho Alta Concentración"), tab_name="Cartucho Alta Concentración")
    create_calculator_ui_in_frame(tabview.tab("Cartucho Baja Concentración"), tab_name="Cartucho Baja Concentración")
    create_calculator_ui_in_frame(tabview.tab("Cartucho Titanio"), tab_name="Cartucho Titanio")
    create_calculator_ui_in_frame(tabview.tab("Termopares"), tab_name="Termopares")
    create_calculator_ui_in_frame(tabview.tab("Bancos de Clima"), tab_name="Bancos de Clima")
    create_calculator_ui_in_frame(tabview.tab("Coilers"), tab_name="Coilers")
    create_calculator_ui_in_frame(tabview.tab("Bandas General Electric"), tab_name="Bandas General Electric")
    create_calculator_ui_in_frame(tabview.tab("Bandas cierre de perno"), tab_name="Bandas cierre de perno")
    create_calculator_ui_in_frame(tabview.tab("Bandas cierre de ceja"), tab_name="Bandas cierre de ceja")
    create_calculator_ui_in_frame(tabview.tab("Bandas medias cañas"), tab_name="Bandas medias cañas")  
   

    app.mainloop()



if __name__ == "__main__":
    run_power_calculator_app()