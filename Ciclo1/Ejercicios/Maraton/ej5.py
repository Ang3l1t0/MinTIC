ki = float(input('Ingrese los km iniciales: '))
kf = float(input('Ingrese los km finales: '))
valor_fijo = 300000

# km recorridos = km finales - km iniciales
kr = kf - ki
if kr <= 3000:
    valor_adicional = 0
elif kr > 3000 and kr <= 10000:
    valor_adicional = ((kr - 3000) * 150)
elif kr > 10000:
    valor_adicional = (((kr - 10000) * 200) + (10000 - 3000) * 150)

total = valor_fijo + valor_adicional
print('El valor a pagar es: $', total)
