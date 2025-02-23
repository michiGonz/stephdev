import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def medium() -> rx.Component:
    return rx.hstack(
        rx.text("3 Years Experience", style=styles.medium_container),
        rx.text("5 Projects Completed", style=styles.medium_container),
        rx.box(
            rx.hstack(
                link_icon(
                    "https://github.com/michiGonz",
                    
                    "/icons/github.svg"      
                ),
                link_icon(
                    "https://linkedin.com/in/stephanie-gonzález-87303a1b6",
                    "/icons/linkedin.svg"
                ),
                link_icon(
                    "https://x.com/stephdev",
                    "/icons/twitter.svg"
                ),
                style={"gap": "20px"}  # Añade espacio entre los iconos
            ),
            style={"display": "flex", "justify-content": "flex-end", "width": "100%", "padding" : "10px"}  # Alinea los iconos a la derecha
        ),
        style=styles.navbar_title_style
    )