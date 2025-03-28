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
        rx.box(
            rx.hstack(
                rx.box(
                    rx.image(src="foto1.png", style=styles.carousel_image_style),
                    rx.link(
                        rx.hstack(
                            rx.text("Project 1"),
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px"})
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
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px"})
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
                            rx.image(src="/icons/github.svg", style={"width": "20px", "height": "20px","margin-right": "10px"})
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
        rx.hstack(
            rx.image(src="php.png", style={"width": "40px", "height": "40px"}),
            rx.image(src="python.png", style={"width": "40px", "height": "40px"}),
            rx.image(src="laravel.png", style={"width": "40px", "height": "40px"}),
            rx.image(src="reflex.jpg", style={"width": "40px", "height": "40px"}),
            rx.image(src="mysql.jpg", style={"width": "40px", "height": "40px","margin-right": "10px"}),
            style=styles.icon_container_style
        ),
        style=styles.about_me_style 
    )