import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles



def header() -> rx.Component:
    return rx.section(
        rx.text("Hi 👋", style=styles.banner_description_style),
        rx.text("I'm a", style=styles.banner_description_style),
        rx.text("Web Developer", style=styles.banner_description_style),
        rx.text("I build things for web", style=styles.banner_description_style
                ),
            rx.hstack(
                link_icon(
                    "https://github.com/michiGonz",
                    "/icons/square.svg"      
                ),
                link_icon(
                    "https://linkedin.com/in/stephanie-gonzález-87303a1b6",
                    "/icons/linkedin.svg"
                ),
                link_icon(
                    "https://x.com/stephdev",
                    "/icons/twitter.svg"
                ),
                style={"gap": "10px","margin-left": "20px", "margin_left": "50px"}  # Añade espacio entre los iconos
            ),
        style=styles.banner_container_style,
    )
