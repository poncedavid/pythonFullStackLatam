
# Python Full Stack Assignments Repository

Este repositorio contiene todas las asignaciones del curso **Python Full Stack**. Cada asignación está diseñada para desarrollar y fortalecer habilidades en tecnologías front-end y back-end, abarcando temas como Flask, MySQL, HTML, CSS, JavaScript, y más.

## Estructura del Repositorio

Cada asignación se encuentra en una carpeta individual con el nombre correspondiente a la tarea. Dentro de cada carpeta, encontrarás el código fuente, archivos de configuración, y cualquier otro recurso necesario para completar la asignación.

### Contenidos del Repositorio

1. **Fundamentos de Flask**
   - **Lotería Mexicana 1 (Core)**: Práctica de recreación de tableros de la lotería mexicana usando Flask, práctica de bucles en plantillas y uso de archivos estáticos.
   - **Tabla de Países (Core)**: Envío de datos desde Flask hacia una plantilla y despliegue de una tabla con estilo CSS.
   - **Visitas (Core)**: Aplicación para contar visitas usando sesiones en Flask.
   - **El juego del destino (Core)**: Formulario en Flask para predecir el futuro del usuario usando sesiones.

2. **ERDs y Consultas SQL**
   - **Estudiantes y Cursos (Core)**: Diagrama de Entidad-Relación (ERD) para manejar la relación de uno a muchos entre estudiantes y cursos.
   - **Canciones (Core)**: ERD para una aplicación de música que gestiona usuarios y sus canciones favoritas (relación muchos a muchos).
   - **Países MySQL (Core)**: Consultas SQL avanzadas en una base de datos de países y ciudades.

3. **CRUDs con Flask y MySQL**
   - **Usuarios CRUD (Core)**: Aplicación CRUD modularizada para manejar usuarios en Flask usando MVC.
   - **Estudiantes y Cursos (Core)**: Aplicación para gestionar cursos y estudiantes, incluyendo formularios y relaciones de uno a muchos.

### Requisitos

Para ejecutar las asignaciones, necesitarás:
- Python 3.x
- MySQL (o un servidor de bases de datos compatible)
- Pipenv para la gestión de dependencias

### Instalación y Configuración

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```
2. Navega a la carpeta de la asignación que deseas ejecutar.
3. Instala las dependencias necesarias:
   ```bash
   pipenv install
   ```
4. Configura tu base de datos en `config/mysqlconnection.py` si la asignación requiere conexión a MySQL.

### Uso

Cada asignación contiene su propio archivo `server.py` o un archivo principal similar que puedes utilizar para ejecutar el proyecto:
```bash
pipenv shell
python server.py
```

### Notas

- Algunas asignaciones pueden requerir que configures tu base de datos ejecutando un archivo `script.sql` ubicado en la carpeta `bd/`.
- Este repositorio se encuentra en desarrollo y puede recibir actualizaciones con nuevas asignaciones o mejoras.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar o agregar algo al repositorio, crea un **pull request** o abre un **issue**.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por revisar este repositorio! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
