# Configuración del Proyecto

## 1. Crear un nuevo proyecto en Flask

Primero, crea una carpeta para el proyecto y navega a ella.

## 2. Crear el entorno virtual con `pipenv`

Ejecuta los siguientes comandos:

```bash
pipenv install flask
pipenv shell
```

## 3. Estructura del proyecto

Dentro de la carpeta del proyecto, crea la siguiente estructura:

CRUD_MOD/
├── bd/
│   └── script.sql         # Script de creación de la base de datos
├── config/
│   └── mysqlconnection.py  # Conexión a la base de datos
├── controllers/
│   └── usuarios.py         # Controlador de usuarios
├── models/
│   └── usuario.py          # Modelo de usuario
├── templates/
│   └── usuarios/           # Carpeta para las plantillas de usuarios
│       ├── index.html      # Lista de usuarios
│       ├── new.html        # Formulario para nuevo usuario
│       ├── edit.html       # Formulario para editar usuario
├── Pipfile
├── Pipfile.lock
└── server.py      

## 4. Probar la Aplicación
Corre el servidor con python server.py.

