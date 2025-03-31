import reflex as rx
from link_bio.styles.styles import Size as Size
import datetime
import requests

# Define el estado para manejar los datos del formulario
class FormState(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""

    def update_name(self, value: str):
        self.name = value

    def update_email(self, value: str):
        self.email = value

    def update_message(self, value: str):
        self.message = value

    def send_message(self):
        try:
            response = requests.post(
                "http://localhost:8000/send-message",  # Cambia la URL según tu configuración
                json={"name": self.name, "email": self.email, "message": self.message}
            )
            if response.status_code == 200:
                print("Mensaje enviado correctamente")
            else:
                print(f"Error al enviar el mensaje: {response.status_code}")
        except requests.RequestException as error:
            print(f"Error al enviar el mensaje: {error}")

# Define el componente del footer
def footer() -> rx.Component:
    return rx.hstack(
        # Cuadro para enviar mensajes
        rx.box(
            rx.text("Send us a message", font_size="20px", font_weight="bold", margin_bottom="10px"),
            rx.input(
                placeholder="Your Name",
                value=FormState.name,  # Asigna el valor directamente desde el estado
                on_change=FormState.update_name,  # Llama al método para actualizar el estado
                style={"margin-bottom": "10px", "width": "100%"}
            ),
            rx.input(
                placeholder="Your Email",
                value=FormState.email,  # Asigna el valor directamente desde el estado
                on_change=FormState.update_email,  # Llama al método para actualizar el estado
                style={"margin-bottom": "10px", "width": "100%"}
            ),
            rx.text_area(
                placeholder="Your Message",
                value=FormState.message,  # Asigna el valor directamente desde el estado
                on_change=FormState.update_message,  # Llama al método para actualizar el estado
                style={"margin-bottom": "10px", "width": "100%", "height": "100px"}
            ),
            rx.button(
                "Send",
                on_click=FormState.send_message,  # Llama al método para enviar el mensaje
                style={"background-color": "#4CAF50", "color": "white", "padding": "10px 20px", "border": "none", "cursor": "pointer"}
            ),
            style={"width": "50%", "padding": "20px", "border": "1px solid #ccc", "border-radius": "5px"}
        ),
        
        # Información de redes sociales
        rx.box(
            rx.image(src="logo.png", height="40px", margin_bottom="10px"),
            rx.link(
                f"© 2014-{datetime.date.today().year} SGDev by Steph G v1.",
                href="https://moure.dev/",
                is_external=True,
                font_size=Size.SMALL.value,
                margin_bottom="10px"
            ),
            rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.", font_size=Size.SMALL.value, margin_bottom="10px"),
            rx.hstack(
                rx.link(rx.image(src="/icons/github.svg", height="30px"), href="https://github.com/michiGonz", is_external=True),
                rx.link(rx.image(src="/icons/linkedin.svg", height="30px"), href="https://linkedin.com/in/stephanie-gonzález-87303a1b6", is_external=True),
                rx.link(rx.image(src="/icons/twitter.svg", height="30px"), href="https://x.com/stephdev", is_external=True),
                style={"gap": "10px"}
            ),
            style={"width": "50%", "padding": "20px", "text-align": "center"}
        ),
        
        align_items="center",  # Centra verticalmente
        justify_content="space-between",  # Espacia horizontalmente
        width="100%",  # Asegura que ocupe todo el ancho
        padding="20px",  # Espaciado interno
        style={"background-color": "#333", "color": "white"}  # Fondo oscuro y texto blanco
    )