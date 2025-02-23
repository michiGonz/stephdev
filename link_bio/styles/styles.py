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
   "background": "linear-gradient(to right, #b47ab2, #af07aa)",
    "padding": "10px",
    "text-align" : "center"
}


#estilo de los links en navbar
navbar_link_style = {
   "color": "white",
   "text-align" : "center",
    "text-decoration": "none",
    "padding": "10px 10px",
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
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "font-weight": "bold",
    "display": "flex",
    "font-size": "14px",
    "background-color": "#1e0225",
    "flex-direction": "row",  
    "justify-content": "center",  # Centra el contenido verticalmente
    "width": "100%",  # Hace que ocupe todo el ancho
    "height": "15vh",  # Hace que ocupe toda la altura de la ventana
    "padding": "10px",
    "padding-bottom":"0px"
}

#estilo del cuadro de sobre mi 
about_me_style = {
    "background-image": "url('/fondo1.png')", 
    "background-size": "cover",  # Asegura que la imagen cubra todo el contenedor
    "background-position": "center",  # Centra la imagen
    "height": "50vh",  # Ocupa el 50% del alto de la ventana
    "width": "100%",  # Ocupa todo el ancho
}

#estilo del texto sobre mi
about_me_text_style = dict (
    text_align ="rigth",
    padding="20px",
)  
        