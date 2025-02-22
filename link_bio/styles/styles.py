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
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
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

# link_bio/styles/styles.py

#logo del navbar
navbar_title_style = {
    "font-size": "24px",
    "font-weight": "bold",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "text-align":"left",
    "padding": "10px"
}

navbar_link_style = {
    "font-size": "16px",
    "font-weight": "normal",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "color": Color.PRIMARY.value,
    "text-decoration": "none",
    "text-align": "center",  # Centrar el texto de los enlaces
    "display": "inline-block",  # Asegurar que el bloque de texto esté centrado
    "width": "100px"  # Ajustar el ancho del enlace
}


banner_text_style = dict(
    font_size = "32px",
    font_weight="bold",
    font_family= "'Helvetica Neue', Arial, sans-serif",
    color= "#FFFFFF",
    margin_bottom="0px"   
)
   
banner_tytlee_style = {
   "font-size": "30px",
    "font-weight": "normal",
    "font-family": "'Sigmar', cursive'",
    "color": "#DDDDDD",
    "margin-bottom": "15px" 
}

banner_subtext_style = {
   "font-size": "25px",
    "font-weight": "normal",
    "font-family": "'Sigmar', cursive'",
    "color": "#DDDDDD",
    "margin-bottom": "10px"  
}


banner_description_style = dict(
    font_size = "40px",
    font_weight = "bold",
    font_family= "'Helvetica Neue', Arial, sans-serif",
    color="#eeeef3",
    margin_left = "60px",
    margin_bottom= "0px"
    
)

# header banner
banner_container_style = {
    "background-image": "url('/assets/banner.png')", 
    "background-size": "cover", 
    "height": "200px",
    "width": "100%"
}


#diseno del texto del medium container
medium_container = {
    "font-size" : "15px",
    "font-weight": "bold",
    "color": "#eeeef3",
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "margin-left": "50px"
}

#medium container style(estilo del medium)
medium_container_style ={
    "font-family": "'Helvetica Neue', Arial, sans-serif",
    "font-weight": "bold",
    "display": "flex",
    "font-size": "14px",
    "background-color": "#1e0225",
    "flex-direction": "row",  
    "justify-content": "center",  # Centra el contenido verticalmente
    "width": "100%",  # Hace que ocupe todo el ancho
    "height": "10vh",  # Hace que ocupe toda la altura de la ventana
    "padding": "10px",
    "padding-bottom":"0px"
}

#estilo de "sobre mi"
about_me_style = {
    "padding":"20px",
    "background-color":"#f0f0f0",
    "text-align":"center" 
}
   
        
        