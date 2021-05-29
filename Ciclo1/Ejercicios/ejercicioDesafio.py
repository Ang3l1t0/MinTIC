facturas = int(input('Introduzca cuantas facturas: '))
numeroFacturas = 0
totalFactura = 0

def subtotal(valorProducto, cantidad):
    subtotal = valorProducto * cantidad
    print('subtotal-->>', subtotal)
    return subtotal

def total(sub):
    total = sub
    print('total', total)


total(subtotal(60, 2))

'''
for i in range(facturas):
    numeroFacturas += 1
    cantidadProductos = int(input('Cuantos productos llevará: '))
    for j in range(cantidadProductos):
        print('Ingrese nombre del producto', (j+1))
        NombreProducto = input()
        print('Cantidad a llevar: ')
        cantidad = int(input())
        print('valor unitario producto', (j+1))
        valorProducto = float(input())
        subtotal(valorProducto, cantidad)
        #totalFactura += subtotal
    print('Numero de factura', numeroFacturas)
    print('Cantidad de productos', cantidadProductos)
    print('------------------------------------')
    print('Total:', totalFactura)
'''