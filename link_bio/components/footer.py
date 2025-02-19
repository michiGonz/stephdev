import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png", 
            margin_top="50px",
            height="40px"
            ),
        rx.link(
            f"© 2014-{datetime.date.today().year} SGDev by Steph G v1.",
            margin_top="0px",
            href="https://moure.dev/",
            is_external=True,
            font_size=Size.SMALL.value,
            
        ),
        rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
        font_size=Size.SMALL.value,
        margin_top="0px",      
                
        ),
       
        color=TextColor.FOOTER.value,
        align_items="center",  # Centra los elementos horizontalmente en el vstack
        justify_content="center",  # Centra los elementos verticalmente en el vstack
        width="100%", # Asegura que el vstack ocupe todo el ancho del contenedor
    ),
   