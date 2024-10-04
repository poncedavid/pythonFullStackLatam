from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
    
    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('tu_base_de_datos').query_db(query)
        return [cls(row) for row in results]

    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('tu_base_de_datos').query_db(query, data)

    @classmethod
    def obtener_por_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('tu_base_de_datos').query_db(query, {'id': id})
        return cls(result[0]) if result else None

    @classmethod
    def actualizar(cls, data):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('tu_base_de_datos').query_db(query, data)

    @classmethod
    def eliminar(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('tu_base_de_datos').query_db(query, {'id': id})
