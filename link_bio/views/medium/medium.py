import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def medium() -> rx.Component:
    return rx.hstack(
        rx.image(src="laravel.png", alt="laravel Icon", width="30px", height="30px"),
        rx.image(src="mysql.png", alt="MySQL Icon", width="30px", height="30px"),        
        rx.image(src="php.png", alt="php Icon", width="30px", height="30px"),
        rx.image(src="reflex.jpg", alt="reflex Icon", width="30px", height="30px"),
        rx.image(src="python.png", alt="python Icon", width="30px", height="30px"),
        style=styles.medium_container_style,
        id="skills-section"  #id único al contenedor
    )