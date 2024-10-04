# Importamos la clase Flask desde el módulo flask para crear nuestra aplicación web
from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Establecemos una clave secreta para la seguridad de la sesión
app.secret_key = "1234"
