import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#constants
MAX_WIDTH="600px"


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


#estilo del logo del navbar
navbar_title_style = {
   "background": "linear-gradient(to right,rgb(206, 162, 204),rgb(59, 12, 58))",
    "padding": "5px",
    "text-align" : "center"
}


#estilo de los links en navbar
navbar_link_style = {
   "color": "white",
   "text-align" : "center",
    "text-decoration": "none",
    "padding": "10px",
    "display": "inline-block",
    "hover": {
            "background-color" : "rgba(255, 255, 255, 0.2)",
        }
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
    "background": "linear-gradient(to right,rgb(206, 162, 204),rgb(59, 12, 58))", #degradado
    "padding": "5px",
    "text-align" : "center",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "font-weight": "bold",
    "display": "flex",
    "font-size": "14px",
    "flex-direction": "row",  
    "justify-content": "center",  # Centra el contenido verticalmente
    "width": "100%",  # Hace que ocupe todo el ancho
    "height": "15vh",  # Hace que ocupe toda la altura de la ventana
    "padding-bottom":"0px"
}

#estilo del cuadro de sobre mi 
about_me_style = {
    "background-image": "url('/fondo1.png')", 
    "background-size": "cover",  # Asegura que la imagen cubra todo el contenedor
    "background-position": "center",  # Centra la imagen
    "height": "100vh",  # Ocupa el 50% del alto de la ventana
    "width": "100%",  # Ocupa todo el ancho
}

#estilo del texto sobre mi
about_me_text_style = dict (
    text_align="right",
    padding="20px",
    white_space="pre-wrap"
) 

carousel_style = {
    "width": "100%",
    "height": "300px",
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
    "box-sizing": "border-box",
    "margin-bottom": "5px" 
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

