'''
En un supermercado un cajero captura los precios de los artículos que los 
clientes compran e indica a cada cliente cuál es el monto de lo que deben pagar.  
Al final del día le indica a su supervisor cuánto fué lo que cobró en total a 
todos los clientes que pasaron por su caja y cual fue el mayor monto de todos.
'''
total = 0
total_compra = 0
clientes = 0
compra_max = 0
producto_max = 0
while True:

    dato = input('Nuevo cliente [s], [salir] or [admin]: ')
    # validaiones
    if dato == 's' or dato == 'S':
        i = 1
        total_compra = 0

        # Pregunto numero de productos a comprar y asigno el valor de la cuenta en un total de compra
        numero_productos = int(input('Igrese cantidad de productos: '))
        while (i <= numero_productos):
            valor_producto = float(input('Ingrese valor del producto: $'))
            total_compra += valor_producto
            if producto_max < valor_producto:
                producto_max = valor_producto
            i += 1
        # acumula los totales de compra para saber cuanto se vendio en el dia e imprime e total de la compra actual
        total += total_compra
        clientes += 1
        print('El valor de su compra es: $', total_compra)
        if total_compra > compra_max:
            compra_max = total_compra
    # Salir del programa
    elif dato == 'salir':
        break
    # Imprime el total de ventas acumuladas del dia
    elif dato == 'admin':
        print('********************** Informe de ventas **********************')
        print('en el dia se ha vendido: $', total)
        print('el numero de clientes atendidos fue:', clientes)
        print('La maxima compra realizada fue de: $', compra_max)
        print('El producto mas caro que se vendio costo: $', producto_max)
    # Si se ingresa un valor no aceptado
    else:
        print('Seleccione un valor valido')
