from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, validators


class Formulario_Login(Form):
    usuario = StringField('Usuario',
                          [
                              validators.DataRequired(
                                  message='Dato requerido.'),
                              validators.Length(
                                  min=8, max=25, message='La longitud debe estar entre 8 y 25 caracteres.')
                          ])
    password = PasswordField('Contraseña',
                             [
                                 validators.DataRequired(
                                     message='Dato requerido.'),
                                 validators.Length(
                                     min=8, max=25, message='La longitud debe estar entre 8 y 25 caracteres.')
                             ])
    recordar = BooleanField('Recordar')
    enviar = SubmitField('Iniciar sesión')
