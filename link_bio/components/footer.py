import reflex as rx
import requests

class FormState(rx.State):
    # Variables para guardar los datos del formulario.
    name: str = ""
    email: str = ""
    message: str = ""
    feedback: str = ""  # Variable para la retroalimentación visual.

    # Método para enviar el formulario al backend Flask.
    def enviar_formulario(self):
        datos = {
            "name": self.name,
            "email": self.email,
            "message": self.message,
        }
        try:
            response = requests.post("http://127.0.0.1:5000/submit", json=datos)
            if response.status_code == 200:
                # Usa el mensaje devuelto o un mensaje por defecto.
                self.feedback = response.json().get("message", "Correo enviado correctamente.")
            else:
                self.feedback = f"Error al enviar el formulario: {response.status_code}"
        except Exception as e:
            self.feedback = f"Hubo un error: {e}"

def FormFooter():
    return rx.box(
        rx.box(
            rx.text("Nombre:", style={"color": "white", "margin-bottom": "5px"}),
            rx.input(
                on_change=FormState.set_name,  # Actualiza el estado directamente.
                placeholder="Tu nombre",
                style={
                    "padding": "10px",
                    "border-radius": "5px",
                    "margin-bottom": "15px",
                    "width": "100%",
                }
            ),
            rx.text("Correo:", style={"color": "white", "margin-bottom": "5px"}),
            rx.input(
                type="email",
                on_change=FormState.set_email,  # Actualiza el estado directamente.
                placeholder="Tu correo",
                style={
                    "padding": "10px",
                    "border-radius": "5px",
                    "margin-bottom": "15px",
                    "width": "100%",
                }
            ),
            rx.text("Mensaje:", style={"color": "white", "margin-bottom": "5px"}),
            rx.text_area(
                on_change=FormState.set_message,  # Actualiza el estado directamente.
                placeholder="Escribe tu mensaje",
                style={
                    "padding": "10px",
                    "border-radius": "5px",
                    "margin-bottom": "15px",
                    "width": "100%",
                }
            ),
            rx.button(
                "Enviar",
                on_click=FormState.enviar_formulario,  # Llama al método de la clase FormState.
                style={
                    "background-color": "#7B4ABF",
                    "color": "white",
                    "border": "none",
                    "padding": "10px 20px",
                    "border-radius": "5px",
                    "cursor": "pointer",
                    "margin-top": "10px",
                },
                hover={"background-color": "#9D65DB"}
            ),
            # Aquí se muestra el mensaje de retroalimentación.
            rx.text(
                FormState.feedback,
                style={"margin-top": "20px", "color": "white", "font-weight": "bold"}
            ),
            style={
                "max-width": "400px",
                "margin": "20px auto",
                "padding": "20px",
                "background-color": "#5D3FD3",
                "border-radius": "10px",
                "color": "white",
                "text-align": "center",
            }
        ),
        style={
            "background-color": "#1F1B24",
            "padding": "40px",
            "color": "white",
        }
    )
