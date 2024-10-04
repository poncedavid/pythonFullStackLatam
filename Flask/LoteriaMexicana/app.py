from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de cartas de la lotería
cartas = [
    "1 El Gallo", "2 El Diablito", "3 La Dama", "4 El Catrín", "5 El Paraguas", 
    "6 La Sirena", "7 La Escalera", "8 La Botella", "9 El Barril", "10 El Árbol", 
    # Continúa la lista...
    "54 La Rana"
]

# Ruta para /loteria que muestra un tablero 4x4
@app.route('/loteria')
def loteria_4x4():
    filas, columnas = 4, 4
    tablero = random.sample(cartas, filas * columnas)
    return render_template('tablero.html', filas=filas, columnas=columnas, tablero=tablero)

# Ruta para /loteria/<x> que muestra un tablero de 4 columnas y x filas
@app.route('/loteria/<int:filas>')
def loteria_filas(filas):
    columnas = 4
    tablero = random.sample(cartas, filas * columnas)
    return render_template('tablero.html', filas=filas, columnas=columnas, tablero=tablero)

# Ruta para /loteria/<x>/<y> que muestra un tablero de x filas y y columnas
@app.route('/loteria/<int:filas>/<int:columnas>')
def loteria_personalizado(filas, columnas):
    tablero = random.sample(cartas, filas * columnas)
    return render_template('tablero.html', filas=filas, columnas=columnas, tablero=tablero)

if __name__ == '__main__':
    app.run(debug=True)
