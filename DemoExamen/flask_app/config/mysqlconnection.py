# Importamos la librería pymysql para interactuar con MySQL
import pymysql.cursors

# Esta clase proporciona una instancia para conectarse a la base de datos MySQL
class MySQLConnection:
    # Método constructor que recibe el nombre de la base de datos como parámetro
    def __init__(self, db):
        # Configuración de la conexión, se pueden ajustar el usuario, la contraseña y otros parámetros según sea necesario
        connection = pymysql.connect(host='localhost',  # Nombre del host (servidor)
                                     user='root',       # Nombre de usuario de la base de datos
                                     password='admin1234',  # Contraseña del usuario de la base de datos
                                     db=db,             # Nombre de la base de datos
                                     charset='utf8mb4', # Codificación de caracteres
                                     cursorclass=pymysql.cursors.DictCursor,  # Los resultados se devuelven como diccionarios
                                     autocommit=True)   # Realiza automáticamente un commit después de cada consulta
        # Se almacena la conexión establecida en un atributo de la clase
        self.connection = connection
    
    # Método para ejecutar consultas SQL en la base de datos
    # Recibe una consulta SQL (query) y opcionalmente datos (data) para consultas parametrizadas
    def query_db(self, query, data=None):
        # Usamos el cursor para interactuar con la base de datos
        with self.connection.cursor() as cursor:
            try:
                # Formateamos la consulta SQL con los datos proporcionados, si los hay
                query = cursor.mogrify(query, data)
                print("Running Query:", query)  # Imprimimos la consulta que se está ejecutando para depuración
                
                # Ejecutamos la consulta en la base de datos
                cursor.execute(query, data)
                
                # Si la consulta es un INSERT, se devuelve el ID de la última fila insertada
                if query.lower().find("insert") >= 0:
                    self.connection.commit()  # Confirmamos la transacción
                    return cursor.lastrowid  # Devolvemos el ID de la nueva fila insertada
                
                # Si es una consulta SELECT, devolvemos el resultado como una lista de diccionarios
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()  # Obtenemos todos los resultados
                    return result  # Devolvemos los resultados
                
                # Si es una consulta UPDATE o DELETE, simplemente confirmamos la transacción
                else:
                    self.connection.commit()  # Confirmamos la transacción
            except Exception as e:
                # Si hay un error, se captura y se imprime el mensaje de error
                print("Something went wrong", e)
                return False  # Devolvemos False si ocurre un error
            finally:
                # Finalmente, cerramos la conexión a la base de datos
                self.connection.close()

# Función para conectar a MySQL, recibe el nombre de la base de datos y crea una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
