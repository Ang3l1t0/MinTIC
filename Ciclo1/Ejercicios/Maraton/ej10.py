ingresos = float(input('Ingrese el valor de sus ingresos: $'))
valor_vivienda = float(input('Ingrese el valor de la vivienda: $'))
meses = 0
if ingresos < 1500000:
    meses = 120
    ci = valor_vivienda * 0.15
    cm = (valor_vivienda - ci) / meses
elif ingresos >= 1500000:
    meses = 84
    ci = valor_vivienda * 0.3
    cm = (valor_vivienda - ci) / meses

print('El cliente debe pagar {} de cuota inicial y {} cuotas de {}'.format(ci, meses, round(cm, 2)))
