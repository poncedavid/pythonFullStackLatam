# Importamos la conexión a MySQL desde la configuración de la aplicación
from flask_app.config.mysqlconnection import connectToMySQL

# Importamos flash para mostrar mensajes de error o validación
from flask import flash 

# Definición de la clase Appointment que representa el modelo de citas en la base de datos
class Appointment:

    # Constructor de la clase, inicializa las propiedades de una cita a partir de un diccionario
    def __init__(self, data):
        # data es un diccionario con los datos de la cita
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

        # Nombre del usuario asociado a la cita
        self.nombre_usuario = data["nombre_usuario"]

    # Método para guardar una nueva cita en la base de datos
    @classmethod
    def save(cls, form):
        # El formulario (form) contiene los datos de la nueva cita
        query = "INSERT INTO appointments (task, date, status, usuario_id) VALUES (%(task)s,%(date)s, %(status)s,%(usuario_id)s)"
        # Ejecutamos la consulta de inserción y devolvemos el ID de la nueva cita
        result = connectToMySQL('belt_exam').query_db(query, form)
        return result

    # Método estático para validar los datos de una cita
    @staticmethod
    def validate_appointment(form):
        # Variable de control que asume que los datos son válidos al inicio
        is_valid = True

        # Validación de que la tarea tenga al menos 2 caracteres
        if len(form["task"]) < 2:
            flash("Task debe tener al menos 2 caracteres", "validate_appointment")
            is_valid = False

        # Validación de que se haya ingresado una fecha
        if form['date'] == "":
            is_valid = False
            flash("Ingresa una fecha de creación", "validate_appointment")

        # Validación de que se haya seleccionado un estado
        if form['status'] == "":
            is_valid = False
            flash("Selecciona un estado", "validate_appointment")

        return is_valid

    # Método para obtener todas las citas de la base de datos
    @classmethod 
    def get_all(cls):
        # Consulta que une las citas con los usuarios correspondientes
        query = "SELECT appointments.* , usuarios.nombre as nombre_usuario FROM appointments JOIN usuarios ON appointments.usuario_id = usuarios.id"
        results = connectToMySQL('belt_exam').query_db(query)  # Lista de diccionarios
        
        # Lista para almacenar las instancias de citas
        appointments = []
        for appointment in results:
            appointments.append(cls(appointment))  # Creamos instancias de Appointment y las agregamos a la lista
        
        return appointments  # Devolvemos la lista de citas

    # Método para obtener una cita por su ID
    @classmethod
    def get_by_id(cls, data):
        # Consulta para obtener una cita por su ID
        query = "SELECT appointments.* , usuarios.nombre as nombre_usuario FROM appointments JOIN usuarios ON appointments.usuario_id = usuarios.id WHERE appointments.id = %(id)s"
        results = connectToMySQL('belt_exam').query_db(query, data)
        appointment = cls(results[0])  # Creamos la instancia de la cita
        return appointment  # Devolvemos la instancia de la cita

    # Método para actualizar una cita en la base de datos
    @classmethod
    def update_appointment(cls, form):
        # Actualizamos los datos de la cita especificada por su ID
        query = "UPDATE appointments SET task = %(task)s, date = %(date)s, status = %(status)s WHERE id  = %(id)s"
        result = connectToMySQL('belt_exam').query_db(query, form)
        return result

    # Método para eliminar una cita de la base de datos
    @classmethod
    def delete_appointment(cls, data):
        # Eliminamos la cita especificada por su ID
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('belt_exam').query_db(query, data)
        return result
