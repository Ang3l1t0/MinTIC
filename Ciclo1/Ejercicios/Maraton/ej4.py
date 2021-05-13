estatura = float(input('Ingrese su estatura en metros: '))
peso = float(input('Ingrese su peso en Kg: '))

imc = round((peso / (estatura**2)), 1)

if imc >= 18.5 and imc <= 24.9:
    riesgo = 'Promedio'
elif imc >= 25 and imc <= 29.9:
    riesgo = 'Aumentado'
elif imc >= 30 and imc <= 34.9:
    riesgo = 'Moderado'
elif imc >= 35 and imc <= 39.9:
    riesgo = 'Severo'
elif imc >= 40:
    riesgo = 'Muy severo'

print('Su IMC:', imc, 'Riesgo:', riesgo)
