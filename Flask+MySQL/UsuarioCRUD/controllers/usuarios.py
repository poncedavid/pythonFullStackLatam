from flask import render_template, redirect, request, session
from models.usuario import Usuario
from flask_app import app

@app.route('/')
def index():
    usuarios = Usuario.obtener_todos()
    return render_template('usuarios/index.html', usuarios=usuarios)

@app.route('/usuarios/nuevo')
def nuevo_usuario():
    return render_template('usuarios/new.html')

@app.route('/usuarios/crear', methods=['POST'])
def crear_usuario():
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.guardar(data)
    return redirect('/')

@app.route('/usuarios/editar/<int:id>')
def editar_usuario(id):
    usuario = Usuario.obtener_por_id(id)
    return render_template('usuarios/edit.html', usuario=usuario)

@app.route('/usuarios/actualizar', methods=['POST'])
def actualizar_usuario():
    data = {
        'id': request.form['id'],
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.actualizar(data)
    return redirect('/')

@app.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    Usuario.eliminar(id)
    return redirect('/')
