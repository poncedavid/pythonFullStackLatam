# Importaciones necesarias para manejar las rutas y sesiones
from flask import Flask, render_template, request, redirect, session
from datetime import datetime, date  # Para manejar fechas

from flask_app import app  # Importamos la instancia de Flask de nuestra aplicación principal

# Importamos los modelos necesarios para interactuar con las citas y los usuarios
from flask_app.models.appointments import Appointment
from flask_app.models.usuarios import Usuario


# Ruta para mostrar el formulario de creación de una nueva cita
@app.route('/new/appointment')
def new_appointment():
    # Verificamos si el usuario ha iniciado sesión
    if 'usuario_id' not in session:
        return redirect("/")  # Si no ha iniciado sesión, lo redirigimos a la página de inicio
    
    # Obtenemos los detalles del usuario utilizando su ID en la sesión
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)

    # Obtenemos la fecha actual para asegurar que las citas se programen en el futuro
    future_date = datetime.now().date()
    
    # Renderizamos el formulario de creación de citas y pasamos la información del usuario y la fecha
    return render_template("new_appointment.html", usuario=usuario, future_date=future_date)


# Ruta para procesar la creación de una nueva cita
@app.route('/create/appointment', methods=["POST"])
def create_appointment():
    # Verificamos si el usuario ha iniciado sesión
    if 'usuario_id' not in session:
        return redirect("/")  # Si no ha iniciado sesión, lo redirigimos al inicio
    
    # Validamos los datos de la cita con el método validate_appointment del modelo Appointment
    if not Appointment.validate_appointment(request.form):
        return redirect("/new/appointment")  # Si la validación falla, redirigimos al formulario
    
    # Si la validación es exitosa, guardamos la nueva cita en la base de datos
    Appointment.save(request.form)
    return redirect("/appointments")  # Redirigimos a la página de citas una vez guardada


# Ruta para mostrar el formulario de edición de una cita
@app.route('/edit/appointment/<int:id>')
def edit_appointment(id):
    # Verificamos si el usuario ha iniciado sesión
    if 'usuario_id' not in session:
        return redirect("/")  # Si no ha iniciado sesión, lo redirigimos al inicio
    
    # Obtenemos los detalles del usuario utilizando su ID en la sesión
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)
    
    # Obtenemos los detalles de la cita a editar por su ID
    data_appointment = {"id": id}
    appointment = Appointment.get_by_id(data_appointment)

    # Verificamos si la cita pertenece al usuario logueado, si no, lo redirigimos al panel de control
    if appointment.usuario_id != session['usuario_id']:
        return redirect("/dashboard")

    # Renderizamos el formulario de edición de citas con los detalles de la cita y el usuario
    return render_template('edit_appointment.html', appointment=appointment, usuario=usuario)


# Ruta para procesar la actualización de una cita
@app.route("/update/appointment", methods=["POST"])
def update_appointment():
    # Verificamos si el usuario ha iniciado sesión
    if 'usuario_id' not in session:
        return redirect("/")  # Si no ha iniciado sesión, lo redirigimos al inicio
    
    # Validamos los datos de la cita actualizada
    if not Appointment.validate_appointment(request.form):
        return redirect("/edit/appointment/" + request.form['id'])  # Si falla, redirigimos al formulario de edición
    
    # Si la validación es exitosa, actualizamos la cita en la base de datos
    Appointment.update_appointment(request.form)
    return redirect("/appointments")  # Redirigimos a la página de citas una vez actualizada


# Ruta para eliminar una cita
@app.route("/delete/appointment/<int:id>")
def delete_appointment(id):
    # Verificamos si el usuario ha iniciado sesión
    if 'usuario_id' not in session:
        return redirect("/")  # Si no ha iniciado sesión, lo redirigimos al inicio
    
    # Eliminamos la cita de la base de datos usando su ID
    data_appointment = {"id": id}
    Appointment.delete_appointment(data_appointment)

    # Redirigimos a la página de citas una vez eliminada la cita
    return redirect("/appointments")
