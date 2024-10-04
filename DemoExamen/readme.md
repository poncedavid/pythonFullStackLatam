# Proyecto Flask 

Este proyecto es una aplicación web que permite a los usuarios gestionar tareas, utilizando Flask como framework web y MySQL como base de datos.

# Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- Python 3.x (https://www.python.org/downloads/)
- MySQL (https://dev.mysql.com/downloads/)

# Pasos para Levantar el Proyecto

## 1. Crear el Modelo de Base de Datos

   1. Abre MySQL Workbench y conéctate a tu servidor local.
   2. Ejecuta el archivo `bd/script.sql`, que se encuentra en la carpeta `bd` del proyecto. Este archivo contiene las sentencias necesarias para crear el esquema de la base de datos.
   
      Pasos para ejecutar el archivo:
      - Abre MySQL Workbench.
      - Selecciona "File" > "Open SQL Script" y navega hasta la carpeta `bd` para seleccionar `script.sql`.
      - Haz clic en el botón de "Execute" (rayito) para ejecutar el script y crear la base de datos.

   3. Asegúrate de que el nombre de la base de datos en MySQL coincida con el nombre que se está utilizando dentro de los modelos `usuarios.py` y `appointments.py`. Revisa o modifica el nombre de la base de datos en el archivo `mysqlconnection.py` si es necesario.
   
      Ejemplo para verificar el nombre de la base de datos en `mysqlconnection.py`:
      ```
      connection = pymysql.connect(host='localhost',
                                   user='root',
                                   password='tu_contraseña',
                                   db='db',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor,
                                   autocommit=True)
      ```

## 2. Crear un Entorno Virtual

   1. Abre una terminal o línea de comandos en la carpeta raíz de tu proyecto.
   2. Ejecuta el siguiente comando para crear un entorno virtual usando `pipenv` e instalar Flask:
      ```
      python -m pipenv install flask
      ```

      Este comando creará un entorno virtual y también instalará Flask dentro de él.

## 3. Activar el Entorno Virtual

   1. Una vez creado el entorno virtual, actívalo con el siguiente comando:
      ```
      python -m pipenv shell
      ```

      Esto te permitirá trabajar dentro del entorno virtual, garantizando que todas las dependencias del proyecto estén aisladas del sistema principal.

## 4. Instalar los Paquetes Necesarios

   1. Dentro del entorno virtual activo, instala los siguientes paquetes ejecutando los comandos uno por uno:
      ```
      pip install pymysql
      pip install flask_bcrypt
      ```

      Estos paquetes son necesarios para la conexión a la base de datos MySQL y para manejar la encriptación de contraseñas.

## 5. Ejecución de la Aplicación

   1. Una vez que el entorno esté configurado y las dependencias instaladas, puedes levantar la aplicación ejecutando el siguiente comando:
      ```
      python server.py
      ```

   2. La aplicación se ejecutará en modo de desarrollo y podrás acceder a ella desde tu navegador en la dirección: http://localhost:5000

## 6. Solución de Problemas

   - Si tienes problemas con la conexión a la base de datos, verifica que la configuración en el archivo `mysqlconnection.py` sea correcta (usuario, contraseña, nombre de la base de datos).
   - Asegúrate de que tu servidor MySQL esté corriendo antes de intentar levantar la aplicación.
