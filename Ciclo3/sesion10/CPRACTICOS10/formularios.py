from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.fields.html5 import EmailField


class Formulario_Contacto(Form):
    nombre = StringField('Nombre')
    email = EmailField('Correo')
    mensaje = StringField('mensaje')
    operador = SelectField("Operador", choices=[("+", "Sumar"), ("-", "Resta"),
                                                ("*", "Multiplicar"), ("/", "Dividir")])
    enviar = SubmitField('Enviar')
