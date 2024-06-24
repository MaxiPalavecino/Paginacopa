from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')

@app.route('/ingresado')
def ingresado():
    return render_template('ingresado.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/deportes')
def deportes():
    return render_template('deportes.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/precios')
def precios():
    return render_template('precios.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

if __name__ == '__main__':
    app.run(debug=True,  port=3500) 
