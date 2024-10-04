# Importaciones necesarias para la funcionalidad del controlador
from flask import Flask, render_template, request, redirect, session, flash  # Importamos funciones esenciales de Flask
from datetime import datetime, date  # Para manejar fechas

from flask_app import app  # Importamos la instancia de Flask de nuestra aplicación principal

# Importamos las clases del modelo para interactuar con los datos de los usuarios y citas
from flask_app.models.usuarios import Usuario
from flask_app.models.appointments import Appointment

# Bcrypt para encriptación de contraseñas
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)  # Inicializamos Bcrypt con la instancia de Flask

# Ruta para la página de inicio que muestra el formulario de login/registro
@app.route('/')
def index():
    return render_template('login_registro.html')  # Renderiza el archivo HTML para login y registro

# Ruta para el proceso de registro
@app.route("/registrar", methods=["POST"])
def registrar():
    # Validamos los datos enviados desde el formulario de registro
    if not Usuario.validar_usuario(request.form):
        return redirect("/")  # Si la validación falla, redirigimos al inicio

    # Encriptamos la contraseña antes de guardarla en la base de datos
    pass_encrypt = bcrypt.generate_password_hash(request.form["password"])

    # Creamos un diccionario con los datos del formulario para enviar al modelo
    form = {
        "nombre": request.form['nombre'],  # Nombre del usuario
        "apellido": request.form['apellido'],  # Apellido del usuario
        "correo": request.form['correo'],  # Correo electrónico
        "password": pass_encrypt  # Contraseña encriptada
    }

    # Guardamos el nuevo usuario en la base de datos y obtenemos su ID
    nuevo_id = Usuario.guardar(form)
    session['usuario_id'] = nuevo_id  # Guardamos el ID del usuario en la sesión
    return redirect("/appointments")  # Redirigimos a la página de citas una vez registrado

# Ruta para la página de citas
@app.route("/appointments")
def appointments():
    # Verificamos que el usuario esté logueado
    if 'usuario_id' not in session:
        return redirect("/")  # Si no está en sesión, lo redirigimos al inicio

    # Preparamos los datos para obtener la información del usuario
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)  # Obtenemos los detalles del usuario por su ID

    # Obtenemos todas las citas de la base de datos
    appointments = Appointment.get_all()

    # Obtenemos la fecha actual para mostrar las citas futuras
    future_date = datetime.now().date()

    # Renderizamos la página de citas con los datos del usuario, citas y la fecha futura
    return render_template("appointments.html", usuario=usuario, appointments=appointments, future_date=future_date)

# Ruta para el proceso de login
@app.route("/login", methods=["POST"])
def login():
    # Obtenemos al usuario por su correo electrónico
    usuario = Usuario.obtener_por_correo(request.form)  # Devuelve una instancia de Usuario o False si no existe

    # Si el correo no está registrado, mostramos un mensaje y redirigimos al inicio
    if not usuario:
        flash("E-mail no registrado", "login")  # Mensaje flash para indicar error en el login
        return redirect("/")

    # Comparamos la contraseña del formulario con la contraseña encriptada almacenada
    if not bcrypt.check_password_hash(usuario.password, request.form["password"]):
        flash("Password incorrecto", "login")  # Mensaje flash si la contraseña es incorrecta
        return redirect("/")

    # Si las credenciales son correctas, guardamos el ID del usuario en la sesión
    session['usuario_id'] = usuario.id
    return redirect("/appointments")  # Redirigimos a la página de citas

# Ruta para cerrar sesión
@app.route("/logout")
def logout():
    session.clear()  # Limpiamos la sesión del usuario
    return redirect("/")  # Redirigimos al inicio
