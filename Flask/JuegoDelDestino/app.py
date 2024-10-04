from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario y almacenar datos en sesión
@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']
    return redirect('/futuro')

# Ruta para mostrar el futuro basado en la información del formulario
@app.route('/futuro')
def futuro():
    # Generar un mensaje aleatorio (positivo o negativo)
    mensaje = random.choice(['buena_suerte', 'mala_suerte'])
    
    if mensaje == 'buena_suerte':
        texto = f"Soy el adivino del Dojo, {session['nombre']} tendrá un viaje muy largo dentro de {session['numero']} años a {session['lugar']} y estará el resto de sus días preparando {session['comida']} para todas las personas que quiere. Cambió de profesión y ahora es {session['profesion']}."
    else:
        texto = f"Soy el adivino del Dojo, {session['nombre']} tendrá {session['numero']} años de mala suerte, nunca conocerá {session['lugar']} y jamás volverá a comer {session['comida']}."
    
    return render_template('futuro.html', texto=texto)

if __name__ == '__main__':
    app.run(debug=True)
