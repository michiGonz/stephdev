import reflex as rx
import requests

class FormState(rx.State):
    # Variables para guardar los datos del formulario
    name: str = ""
    email: str = ""
    message: str = ""

    # Método para enviar el formulario al backend Flask
    def enviar_formulario(self):
        datos = {
            "name": self.name,
            "email": self.email,
            "message": self.message,
        }
        try:
            response = requests.post("http://127.0.0.1:5000/submit", json=datos)
            if response.status_code == 200:
                print(response.json()["message"])
            else:
                print("Error al enviar el formulario:", response.status_code)
        except Exception as e:
            print(f"Hubo un error al enviar el formulario: {e}")
