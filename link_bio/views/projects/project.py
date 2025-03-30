import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def project() -> rx.Component:
    return rx.vstack(
        # Título "Projects" centrado
        rx.text("Projects", style=styles.about_me_title_style),  # Aplica un nuevo estilo para centrar el título

        # Carrusel de proyectos
        rx.box(
            rx.hstack(
                rx.box(
                    rx.image(src="foto1.png", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 1"),
                            rx.image(src="/icons/squar.svg", style={"width": "20px", "height": "20px"})
                        ),
                        href="https://github.com/michiGonz/proyectoSISG",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                rx.box(
                    rx.image(src="foto2.png", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 2"),
                            rx.image(src="/icons/squar.svg", style={"width": "20px", "height": "20px"})
                        ),
                        href="https://github.com/michiGonz/Corpoelec_sistema",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                rx.box(
                    rx.image(src="foto3.png", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 3"),
                            rx.image(src="/icons/squar.svg", style={"width": "20px", "height": "20px", "margin-right": "10px"})
                        ),
                        href="https://github.com/michiGonz/stephdev",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                style=styles.carousel_style
            ),
            style={"width": "100%"}
        ),
        style=styles.project_style  # Aplica un estilo general para centrar todo
    )