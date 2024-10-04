from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

# Ruta principal: muestra las visitas
@app.route('/')
def index():
    if 'visitas' not in session:
        session['visitas'] = 0
        session['reinicios'] = 0  # Contador de reinicios
    else:
        session['visitas'] += 1
    return render_template('index.html', visitas=session['visitas'], reinicios=session['reinicios'])

# Ruta para eliminar la sesión y redirigir a la raíz
@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()  # Elimina todas las propiedades de la sesión
    return redirect('/')

# Ruta para sumar 2 visitas
@app.route('/sumar2')
def sumar2():
    if 'visitas' in session:
        session['visitas'] += 2
    return redirect('/')

# Ruta para reiniciar el contador de visitas
@app.route('/reiniciar')
def reiniciar():
    session['visitas'] = 0
    session['reinicios'] += 1  # Aumenta el número de reinicios
    return redirect('/')

# Ruta para sumar un número ingresado por el usuario
@app.route('/sumar', methods=['POST'])
def sumar():
    if 'visitas' in session:
        suma = int(request.form['cantidad'])
        session['visitas'] += suma
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
