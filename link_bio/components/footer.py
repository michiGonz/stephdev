import reflex as rx
from link_bio.styles.styles import Size as Size
import datetime

# Define el componente del footer
def footer() -> rx.Component:
    return rx.hstack(
        # Información de redes sociales y texto
        rx.box(
            rx.image(src="logo.png", height="50px", margin_bottom="20px"),
            rx.link(
                f"© 2014-{datetime.date.today().year} SGDev by Steph G v1.",
                href="https://moure.dev/",
                is_external=True,
                font_size=Size.SMALL.value,
                margin_bottom="10px",
                style={"color": "#aaa", "text-decoration": "none"}
            ),
            rx.text(
                "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                font_size=Size.SMALL.value,
                margin_bottom="20px",
                style={"color": "#aaa"}
            ),
            rx.hstack(
                rx.link(
                    rx.image(src="/icons/github.svg", height="30px"),
                    href="https://github.com/michiGonz",
                    is_external=True,
                    style={"margin": "0 10px"}
                ),
                rx.link(
                    rx.image(src="/icons/linkedin.svg", height="30px"),
                    href="https://linkedin.com/in/stephanie-gonzález-87303a1b6",
                    is_external=True,
                    style={"margin": "0 10px"}
                ),
                rx.link(
                    rx.image(src="/icons/twitter.svg", height="30px"),
                    href="https://x.com/stephdev",
                    is_external=True,
                    style={"margin": "0 10px"}
                ),
                style={"justify-content": "center", "gap": "15px"}
            ),
            style={
                "width": "50%",
                "padding": "20px",
                "text-align": "center",
                "color": "white"
            }
        ),
        # Formulario para enviar un mensaje
        rx.box(
            rx.text(
                "Envíanos un mensaje",
                font_size=Size.LARGE.value,
                margin_bottom="20px",
                style={"color": "white", "font-weight": "bold"}
            ),
            rx.form(
                rx.input(
                    placeholder="Tu nombre",
                    name="name",
                    style={
                        "width": "100%",
                        "margin-bottom": "15px",
                        "padding": "10px",
                        "border": "1px solid #555",
                        "border-radius": "5px",
                        "background-color": "#444",
                        "color": "white"
                    }
                ),
                rx.input(
                    placeholder="Tu correo electrónico",
                    name="email",
                    type="email",
                    style={
                        "width": "100%",
                        "margin-bottom": "15px",
                        "padding": "10px",
                        "border": "1px solid #555",
                        "border-radius": "5px",
                        "background-color": "#444",
                        "color": "white"
                    }
                ),
                rx.text_area(
                    placeholder="Escribe tu mensaje aquí...",
                    name="message",
                    style={
                        "width": "100%",
                        "margin-bottom": "15px",
                        "padding": "10px",
                        "border": "1px solid #555",
                        "border-radius": "5px",
                        "background-color": "#444",
                        "color": "white",
                        "min-height": "100px"
                    }
                ),
                rx.button(
                    "Enviar",
                    type="submit",
                    style={
                        "background-color": "#555",
                        "color": "white",
                        "padding": "10px 20px",
                        "border": "none",
                        "border-radius": "5px",
                        "cursor": "pointer",
                        "font-weight": "bold"
                    },
                    hover_style={
                        "background-color": "#777"
                    }
                ),
                action="/send_message",  # Ruta para manejar el envío del mensaje
                method="post",
                style={"width": "100%", "margin-top": "20px"}
            ),
            style={
                "width": "50%",
                "padding": "20px",
                "text-align": "center",
                "background-color": "#222",
                "border-radius": "10px"
            }
        ),
        align_items="center",        justify_content="space-between",        width="100%",        padding="40px",        style={"background-color": "#333", "color": "white"}    )