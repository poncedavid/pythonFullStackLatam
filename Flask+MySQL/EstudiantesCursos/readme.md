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

estudiantes_cursos/
├── bd/
│   └── script.sql
├── config/
│   └── mysqlconnection.py
├── controllers/
│   ├── cursos.py
│   └── estudiantes.py
├── models/
│   ├── curso.py
│   └── estudiante.py
├── templates/
│   ├── cursos/
│   │   ├── index.html
│   │   └── mostrar.html
│   └── estudiantes/
│       └── nuevo.html
├── Pipfile
├── Pipfile.lock
└── server.py

## 4. Probar la Aplicación
Corre el servidor con python server.py.

