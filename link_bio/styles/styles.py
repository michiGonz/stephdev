import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

STYLESHEETS = []

#constants
MAX_WIDTH="600px"

#animaciones al archivo CSS global
STYLESHEETS.append("""
@keyframes glow {
    0% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 60px #ff00ff; }
    50% { text-shadow: 0 0 10px #fff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 70px #ff00ff, 0 0 80px #ff00ff; }
    100% { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 60px #ff00ff; }
}

@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
""") 

#sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    LARGE = "4"
    BIG = "5"

STYLESHEETS =[
    "https://fonts.googleapis.com/css?family=Roboto:wght@300&display=swap"
]

#styles

BASE_STYLE ={
    "font_family": Font.DEFAULT.value, #fuente general
    "background_color": Color.BACKGROUND.value, #color de fondo general
    "scroll_behavior": "smooth",  # Habilita el desplazamiento suave
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display" :"block",
        "padding": Size.SMALL.value,
        "border_radius": "20px",
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
          "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}
title_style = dict(
    padding_top="20px",
    Color=TextColor.BODY.value,
    width="100%"
)

button_title_styles = dict(
    font_size=Size.SMALL.value,
    color=TextColor.HEADER.value
)

button_body_styles = dict(
    font_size= Size.BIG.value,
     color=TextColor.BODY.value
)


#estilo del navbar
navbar_style = {
    "display": "flex",  # Usa flexbox
    "align-items": "center",  # Alinea verticalmente
    "justify-content": "space-between",  # Distribuye los elementos a los extremos
    "width": "100%",  # Ocupa todo el ancho
    "padding": "10px 20px",  # Espaciado interno
    "position": "absolute",  # Posición absoluta dentro del header
    "top": "0",  # Posición superior
    "margin-bottom": "50px",  # Espacio debajo del navbar
}

# Estilo del logo
navbar_logo_style = {
    "width": "50px",  # Tamaño del logo
    "height": "50px",  # Tamaño del logo
    "object-fit": "contain",  # Asegura que no se distorsione
}

# Estilo del contenedor de los enlaces
navbar_links_container_style = {
    "display": "flex",  # Usa flexbox
    "gap": "20px",  # Espaciado entre los enlaces
}


# Estilo de los enlaces del navbar
navbar_link_style = {
    "color": "white",  # Color del texto
    "text-decoration": "none",  # Sin subrayado
    "font-size": "16px",  # Tamaño de fuente
    "font-weight": "bold",  # Negrita
    "padding": "5px 10px",  # Espaciado interno
    "border-radius": "5px",  # Bordes redondeados
    "transition": "background-color 0.3s",  # Transición suave
    "_hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",  # Fondo al pasar el mouse
    },
}

#estilo del texto de la descripcion del banner
banner_description_style = dict(
    font_size = "40px",
    font_weight = "bold",
    font_family= "'Helvetica Neue', Arial, sans-serif",
    color="#eeeef3",
    margin_left = "60px",
    margin_bottom= "0px"
    
)

# estilo del banner
banner_container_style = dict (
    background_image = "url('/banner.png')",
    background_size = "cover",
    background_position = "center",
    height = "auto",
    width = "100%",
)

#diseno del texto del medium container
medium_container = {
    "font-size" : "15px",
    "font-weight": "bold",
    "color": "#eeeef3",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "margin-left": "50px"
}

#medium container style(estilo del elemento del medio(medium)
medium_container_style ={
    "background": "linear-gradient(to right, rgb(206, 162, 204), rgb(59, 12, 58))",  # Degradado
    "padding": "0px 10px",  # Ajusta el padding para eliminar el espacio superior
    "display": "flex",
    "flex-direction": "row",
    "justify-content": "flex-end",  # Alinea los íconos a la derecha
    "align-items": "center",  # Centra los íconos verticalmente
    "height": "9vh",  # Altura del contenedor
    "width": "100%",  # Ancho completo
}

# Estilo para el título "About Me"
about_me_title_style = {
    "color": "white",  # Color blanco
    "font-size": "3em",  # Tamaño grande
    "font-weight": "bold",  # Negrita
    "text-align": "center",  # Centrado
    "animation": "glow 1.5s infinite, fadeIn 3s",  # Efecto brillante y aparición progresiva
    "margin": "0 auto",  # Centrado horizontal
}

#estilo del cuadro de sobre mi (content)
about_me_style = {
    "background-image": "url('/about.png')", 
    "background-size": "cover", 
    "background-position": "center",  
    "background-attachment": "fixed",  
    "height": "60vh",  # Ocupa el 50% del alto de la ventana
    "width": "100%",  # Ocupa todo el ancho
}

#estilo del texto sobre mi
about_me_text_style = {
    "text_align": "center",  # Centra el texto horizontalmente
    "padding": "20px",  # Espaciado interno
    "white_space": "pre-wrap",  # Mantiene los saltos de línea
    "font-weight": "bold",  # Negrita
    "color": "white",  # Color blanco
    "display": "flex",  # Usa flexbox para centrar
    "justify-content": "center",  # Centra horizontalmente
    "align-items": "center",  # Centra verticalmente
    "height": "100%",  # Asegura que ocupe todo el contenedor
}
   

carousel_style = {
    "width": "100%",
    "height": "255px",
    "display": "flex",
    "overflow": "hidden",
    "position": "relative",
    "justify-content": "flex-end",
    "margin": "20px 0"
}

# estilo de los elementos del carrusel
carousel_item_style = {
    "width": "200px",  # Ajusta el ancho del cuadrado
    "height": "250px",  # Ajusta la altura del cuadrado
    "transition": "transform 0.5s ease-in-out",
    "text-align": "center",
    "display": "flex",
    "flex-direction": "column",
    "align-items": "center",
    "justify-content": "center",
    "border": "1px solid #ccc",
    "padding": "10px",
    "margin-right": "10px",
    "box-sizing": "border-box",
}
# estilo de las imágenes del carrusel
carousel_image_style = {
    "width": "100%",  # Ajusta el ancho de la imagen
    "height": "150px",  # Ajusta la altura de la imagen
    "object-fit": "cover"  # Asegura que la imagen cubra el contenedor sin distorsionarse
}

# estilo de los enlaces del carrusel
carousel_link_style = {
    "color": "blue",
    "text-decoration": "none",
    "display": "block",
    "margin-top": "10px"
}

# estilo del contenedor de los iconos debajo del carrusel
icon_container_style = {
    "width": "100%",
    "height": "300px",
    "display": "flex",
    "overflow": "hidden",
    "position": "relative",
    "justify-content": "flex-end",
    "margin": "20px 0",
    "object-fit": "cover"
    
}

