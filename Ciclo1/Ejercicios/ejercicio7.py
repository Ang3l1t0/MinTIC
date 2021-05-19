# Factorial de n numeros
# catidad de numeros a los que se les scara el factorial
veces = int(input('Introduzca la cantidad de factoriales a realizar: '))
while veces > 0:
    num = int(input("Introduzca un numero: "))
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num - 1
    veces -= 1
    print(factorial)
