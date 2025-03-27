import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles

def content() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text("About Me", style={"font-size": "2em", "font-weight": "bold", "text-align": "right", "padding": "20px"}),
            rx.text(
                "Hi, I'm [Your Name]. I'm passionate about [Your Passion or Field].\n"
                "I love working on projects that involve [Brief Description of What You Do].\n"
                "In my free time, I enjoy [Your Hobbies or Interests].",
                style=styles.about_me_text_style
            ),
            style={"width": "100%"}  # Asegura que el contenedor ocupe todo el ancho disponible
        ),
        rx.box(
            rx.hstack(
                rx.box(
                    rx.image(src="foto1.jpg", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 1"),
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px"})
                        ),
                        href="https://github.com/michiGonz/project1",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                rx.box(
                    rx.image(src="foto2.jpg", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 2"),
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px"})
                        ),
                        href="https://github.com/michiGonz/project2",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                rx.box(
                    rx.image(src="foto2.jpg", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 3"),
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px"})
                        ),
                        href="https://github.com/michiGonz/project3",
                        style=styles.carousel_link_style
                    ),
                    style=styles.carousel_item_style
                ),
                style=styles.carousel_style
            ),
            style={"width": "100%"}
        ),
        rx.hstack(
            rx.image(src="php.png", style={"width": "60px", "height": "60px"}),
            rx.image(src="python.png", style={"width": "60px", "height": "60px"}),
            rx.image(src="laravel.png", style={"width": "60px", "height": "60px"}),
            style=styles.icon_container_style
        ),
        style=styles.about_me_style 
    )