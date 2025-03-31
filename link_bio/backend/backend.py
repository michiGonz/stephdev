from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
app = Flask(__name__)



load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Configuración del correo
SMTP_SERVER = "smtp.gmail.com"  # Cambia esto si usas otro proveedor
SMTP_PORT = 587
EMAIL_ADDRESS = "stephaniemgonzalez10@gmail.com"  # Reemplaza con tu correo
EMAIL_PASSWORD = "ljyb cxmr zorv vqqq"  # Reemplaza con tu contraseña (usa contraseñas de aplicación si es necesario)

@app.route("/send-message", methods=["POST"])
def send_message():
    # Obtener los datos del formulario
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # Validar los datos
    if not name or not email or not message:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        # Crear el mensaje de correo
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS  # Puedes enviar el correo a ti mismo
        msg["Subject"] = f"Nuevo mensaje de {name}"

        body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"
        msg.attach(MIMEText(body, "plain"))

        # Enviar el correo
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return jsonify({"success": "Mensaje enviado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)