import reflex as rx
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Obtener las credenciales del archivo .env
SENDER_EMAIL = os.getenv("EMAIL_USER")
RECEIVER_EMAIL = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Función para manejar el envío del mensaje
def send_message(name: str, email: str, message: str):
    try:
        # Configurar el mensaje de correo
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = "Nuevo mensaje desde el formulario"

        # Contenido del correo
        body = f"""
        Has recibido un nuevo mensaje:
        Nombre: {name}
        Correo: {email}
        Mensaje: {message}
        """
        msg.attach(MIMEText(body, "plain"))

        # Enviar el correo usando SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        return rx.alert("Mensaje enviado correctamente.", status="success")
    except Exception as e:
        return rx.alert(f"Error al enviar el mensaje: {e}", status="error")

# Define la aplicación Reflex
app = rx.App()

@app.route("/send_message", methods=["POST"])
def handle_form_submission(request):
    # Obtener los datos enviados desde el formulario
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Llamar a la función para enviar el correo
    return send_message(name, email, message)

# Agregar la página del footer
app.add_page("footer", route="/")
app.compile()