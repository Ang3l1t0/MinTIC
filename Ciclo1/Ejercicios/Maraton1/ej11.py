estado = True
while estado:
    opcion=input("Desea ver otro mensaje [s] [n]: ")
    if opcion == "n" or opcion == "N":
        estado=False
    elif opcion == "s" or opcion == "S":
        print("hola")
    else:
        print("Solo se admite \"s\" o \"n\"")      
print("---Fin---")
