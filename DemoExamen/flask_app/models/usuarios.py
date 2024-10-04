# Importamos la conexión a MySQL desde la configuración de la aplicación
from flask_app.config.mysqlconnection import connectToMySQL

# Importamos flash para mostrar mensajes de error
from flask import flash

# Importamos la librería de expresiones regulares para validar correos electrónicos
import re

# Expresión regular para validar la estructura de un correo electrónico
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Definición de la clase Usuario, que representa el modelo de usuarios en la base de datos
class Usuario:

    # Constructor de la clase, inicializa las propiedades del usuario a partir de un diccionario
    def __init__(self, data):
        # data es un diccionario con los datos del usuario
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Método para guardar un nuevo usuario en la base de datos
    @classmethod
    def guardar(cls, form):
        # El formulario (form) contiene los datos del nuevo usuario
        query = "INSERT INTO usuarios (nombre, apellido, correo, password) VALUES (%(nombre)s,%(apellido)s, %(correo)s,%(password)s)"
        # Ejecutamos la consulta de inserción y devolvemos el ID del nuevo usuario
        result = connectToMySQL('belt_exam').query_db(query, form)
        return result

    # Método estático para validar los datos de registro del usuario
    @staticmethod
    def validar_usuario(form):
        # Variable de control que asume que los datos son válidos al inicio
        is_valid = True

        # Validación de que el nombre tenga al menos 2 caracteres
        if len(form["nombre"]) < 2:
            flash("Nombre debe tener al menos 2 caracteres", "register")
            is_valid = False

        # Validación de que el apellido tenga al menos 2 caracteres
        if len(form["apellido"]) < 2:
            flash("Apellido debe tener al menos 2 caracteres", "register")
            is_valid = False
        
        # Validación del formato del correo electrónico usando la expresión regular
        if not EMAIL_REGEX.match(form["correo"]):
            flash("E-mail inválido", "register")
            is_valid = False
        
        # Validación de que el correo sea único (no registrado previamente)
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s"
        results = connectToMySQL('belt_exam').query_db(query, form)
        if len(results) >= 1:
            flash("E-mail registrado previamente", "register")
            is_valid = False
        
        # Validación de que la contraseña tenga al menos 6 caracteres
        if len(form["password"]) < 8:
            flash("Contraseña debe tener al menos 6 caracteres", "register")
            is_valid = False

        # Validación de que las contraseñas coincidan
        if form["password"] != form["confirm"]:
            flash("Las contraseñas no coinciden", "register")
            is_valid = False

        return is_valid

    # Método para obtener un usuario por su correo electrónico
    @classmethod
    def obtener_por_correo(cls, form):
        # Consulta para obtener el usuario por correo
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s"
        results = connectToMySQL('belt_exam').query_db(query, form)
        
        # Si el usuario existe, devolvemos la instancia del usuario
        if len(results) == 1:
            usuario = cls(results[0])
            return usuario
        else:
            return False

    # Método para obtener un usuario por su ID
    @classmethod
    def obtener_por_id(cls, form):
        # Consulta para obtener el usuario por ID
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query, form)
        # Retornamos la instancia del usuario encontrado
        usuario = cls(results[0])
        return usuario

    # Método para mostrar todos los usuarios de la base de datos
    @classmethod
    def muestra_usuarios(cls):
        # Consulta para obtener todos los usuarios
        query = "SELECT * FROM usuarios"
        results = connectToMySQL('usuarios').query_db(query)
        
        # Creamos una lista para almacenar las instancias de usuarios
        usuarios = []
        for us in results:
            usuario = cls(us)  # Instanciamos cada usuario con sus datos
            usuarios.append(usuario)  # Agregamos cada usuario a la lista
        
        return usuarios  # Devolvemos la lista de objetos Usuario

    # Método para eliminar un usuario por su ID
    @classmethod
    def borrar(cls, diccionario):
        query = "DELETE FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('usuarios').query_db(query, diccionario)
        return result

    # Método para obtener los datos de un usuario por su ID
    @classmethod
    def mostrar(cls, diccionario):
        query = "SELECT * FROM usuarios WHERE id = %(id)s"
        result = connectToMySQL('usuarios').query_db(query, diccionario)
        usuario = cls(result[0])
        return usuario

    # Método para actualizar los datos de un usuario
    @classmethod
    def actualizar(cls, formulario):
        # Actualizamos los datos del usuario con el ID especificado
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido=%(apellido)s, correo=%(correo)s WHERE id=%(id)s"
        result = connectToMySQL('usuarios').query_db(query, formulario)
        return result
