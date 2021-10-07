from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect, url_for
from utils import isUsernameValid, isEmailValid, isPasswordValid
import yagmail as yagmail
from forms import Formulario_Login

app = Flask(__name__)
app.secret_key = "Ronald"


@app.route('/')
@app.route('/index')
def index():
    return render_template("registro.html")


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    titulo = 'Registro'
    try:
        if request.method == 'POST':
            usuario = request.form['usuario']
            email = request.form['email']
            password = request.form['password']

            error = None

            # 1 Validar aquí en el servidor.
            if not isUsernameValid(usuario):
                # Está mal
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
            if not isEmailValid(email):
                # Está mal
                error = "Correo invalido"
                flash(error)
            if not isPasswordValid(password):
                # Está mal
                error = "La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres"
                flash(error)

            if error is not None:
                return render_template("registro.html", titulo=titulo)
            else:
                # 2 Enviar un correo.
                # Para crear correo:
                # Modificar la siguiente linea con tu informacion personal
                # pehernaldo2@gmail.com  Hernaldo12345678*
                yag = yagmail.SMTP('pehernaldo2@gmail.com',
                                   'Hernaldo12345678*')
                yag.send(to=email, subject='Activa tu cuenta',
                         contents='Bienvenido, usa este link para activar tu cuenta ')
                flash('Revisa tu correo para activar tu cuenta')

                # 3 Abrir el formulario Login.
                return redirect(url_for('login'))

            # Tarea crear un correo de GMail para probar lo del envío de correo.
            return "Entró a registro por POST. " + usuario + email + password

        return render_template("registro.html", titulo='Registro')
    except:
        flash('Un error no identificado.')
        return render_template("registro.html", titulo='Registro')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Formulario_Login(request.form)
    if request.method == 'POST' and form.validate():
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(
            form.usuario.data, form.recordar.data))
        return redirect(url_for('gracias'))

    # Entró por GET
    return render_template("login.html", form=form, titulo='Inicio de sesión')


@app.route('/gracias', methods=['GET', 'POST'])
def gracias():
    return render_template("gracias.html", titulo='Gracias')
