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

├── app.py
├── static
│   └── style.css
└── templates
    └── tablero.html

## 4. Probar la Aplicación
Corre el servidor con python app.py.

Visita las diferentes rutas:

/loteria → Muestra un tablero 4x4.
/loteria/5 → Muestra un tablero de 4x5.
/loteria/5/6 → Muestra un tablero de 5x6.

Esto cubre los 4 niveles de la tarea, con el bonus de asignar cartas aleatorias del listado proporcionado.