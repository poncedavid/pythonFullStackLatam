# Importamos la aplicación Flask desde el paquete flask_app
from flask_app import app

# Importamos los controladores que gestionan las rutas relacionadas con los usuarios y las citas
from flask_app.controllers import users_controllers
from flask_app.controllers import appointments_controllers

# Verificamos si el archivo se está ejecutando directamente para iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)  # Iniciamos el servidor en modo depuración (debug)
