from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from formularios import Formulario_Contacto
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    form = Formulario_Contacto(request.form)
    return render_template("contacto.html", form=form)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    flash(app.secret_key)
    form = Formulario_Contacto(request.form)
    if request.method == 'POST':
        flash(form.nombre.data)
        flash(form.email.data)
        flash(form.mensaje.data)
    return render_template("contacto.html", form=form)
