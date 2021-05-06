'''
ejercicio1:
la jefe de nomina desea saber cual sera el total a pagar
de un empleado que trabajo en el dia 12 horas durante 5 dias
en la empresa se cataloga que hasta 8 horas diarias son tomadas
 como horas ordinarias y cada hora ordinaria tiene
un pago "X" , despues de las 8 horas diarias se cataloga
como hora extra y tiene un valor de hora adicional que seria
de 5000 pesos.
se desea saber cual seria el pago total que recibira
ese empleado a los 5 dias.
'''

horas = float(input('Ingrese el numero de horas diarias trabajadas: '))
valor_hora = float(input('Ingrese el valor de la hora ordinaria: '))
dias_laborados = int(
    input('Ingrese la cantidad de dias que laboró la persona: '))

tiempo_extra = 0
horas_ordinarias = 8

# obtengo la cantidad de las horas extras
horas_extras = horas - horas_ordinarias

# calculo el valor de las horas extras
valor_extra = (horas_extras * (5000 + valor_hora))

# el total 8 horas ordinarias + el valor de las extras * los dias laborados
total = ((valor_extra + (horas_ordinarias * valor_hora)) * dias_laborados)
print('Salario a pagar es:', total)
