from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

# Ruta GET para comprobar que el servidor esté activo.
@app.route("/", methods=["GET"])
def index():
    return "El backend está corriendo correctamente. Utiliza el endpoint /submit para enviar datos."

# Ruta POST para procesar el formulario y enviar el correo.
@app.route("/submit", methods=["POST"])
def submit():
    # Recupera los datos enviados en formato JSON.
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    try:
        # Configura la conexión SMTP.
        # En este ejemplo se usa Gmail; asegúrate de tener configurada la verificación en dos pasos y usar una contraseña de aplicación.
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # Cambia 'tu_correo@gmail.com' y 'tu_contraseña' por tus credenciales reales.
        server.login("stephaniemgonzalez10@gmail.com", "bfepesrcfpdtwsos")
        
        # Prepara el mensaje de correo.
        subject = "Nuevo mensaje del formulario"
        body = f"Nombre: {name}\nCorreo: {email}\nMensaje: {message}"
        email_message = f"Subject: {subject}\n\n{body}"
        
        # Envía el correo:
        # - El primer parámetro es el correo del remitente (debe ser el mismo que usas para loguearte).
        # - El segundo parámetro es el correo de destino (puede ser una lista de correos).
        server.sendmail("stephaniemgonzalez10@gmail.com", "fefigonzalez610@gmail.com", email_message)
        server.quit()
        
        return jsonify({"message": "Correo enviado correctamente."})
    except Exception as e:
        # En caso de error, devuelve una respuesta JSON con el mensaje de error.
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
