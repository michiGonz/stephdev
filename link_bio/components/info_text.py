import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold", 
            color="blue", 
            as_="span"),
        
        rx.text(body, font_size=Size.BIG.value, as_="span"),
       
        color=TextColor.BODY.value,
        
        style={
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "gap": "10px"  # Ajusta el valor según el espacio que desees
        }
    )
    