import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def content() -> rx.Component:
    return rx.hstack(
        rx.box(
                rx.text("About Me", style={"font-size": "2em", "font-weight": "bold"}),
                rx.text("Hi, I'm [Your Name]. I'm passionate about [Your Passion or Field]. I love working on projects that involve [Brief Description of What You Do]. In my free time, I enjoy [Your Hobbies or Interests]."),
            style=styles.about_me_style
            ),
        
        style={"gap": "20px"}  # Añade espacio entre los contenedores
    )