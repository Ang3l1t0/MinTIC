from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Hola Mundo! Soy Angel'

@app.route('/persona/')
def persona():
    return 'Hola entró por persona'

@app.route('/cliente/')
def cliente():
    return 'Hola soy el cliente'

@app.route('/suma/<int:n1>/<int:n2>/')
def suma(n1, n2):
    return str(n1 + n2)

@app.route('/suma/', methods=['GET', 'POST'])
def suma_formulario():
    if  request.method == 'POST':      
        v_n1 = int(request.form['n1'])
        v_n2 = int(request.form['n2'])
        resultado = v_n1 + v_n2
        return render_template("suma.html", resultado=resultado)      
    # fue por GET:
    return render_template("suma.html")

@app.route('/estudiante/')
@app.route('/estudiante/<nombre>/')
@app.route('/estudiante/<nombre>/<apellido>/')
@app.route('/estudiante/<nombre>/<apellido>/<int:edad>/')
def estudiante(nombre=None, apellido=None, edad=None):
    return f"Entro en estudiante. <br>Nombre: {nombre} <br>Apellido: {apellido} <br>Edad: {edad}"