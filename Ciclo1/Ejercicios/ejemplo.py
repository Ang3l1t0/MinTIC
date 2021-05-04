nombre = input("Ingrese el nombre y apellido del estudiante: ")
nota1 = int(input("Ingrese el valor de la Nota 1: "))
nota2 = int(input("Ingrese el valor de la Nota 2: "))
nota3 = int(input("Ingrese el valor de la Nota 3: "))

nota = ((nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5))
print("La nota final de {} es de {}".format(nombre, nota))
