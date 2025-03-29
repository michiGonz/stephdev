import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def content() -> rx.Component:
    return rx.vstack(
        rx.box(
           rx.text("About Me", style=styles.about_me_title_style),  # Aplica el nuevo estilo
            rx.text(
                "Hi, My name is Stephanie Gonzalez, I am a freelance computer\n",
                "scientist entrepreneur and technology lover.\n",
                "My main skills are project architecture, consulting and software development focused,\n",
                "above all, on iOS, Android and web applications.\n",
                "Since much of my professional career has been dedicated to enterprise software,\n",
                "I also perform these same tasks applied to backend design and development.\n",
                style=styles.about_me_text_style
            ),
            style={"width": "100%"}  # Asegura que el contenedor ocupe todo el ancho disponible
        ),
        style=styles.about_me_style 
    )