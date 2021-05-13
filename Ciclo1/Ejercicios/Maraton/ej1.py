valor_compra = int(input('Ingrese el valor total de la compra: '))
descuento = 0.8
valor_asignado = 200000

if valor_compra > valor_asignado:
    total = valor_compra * descuento
else:
    total = valor_compra
print(total)
