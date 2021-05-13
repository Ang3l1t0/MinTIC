print("Registro postulantes del programa 'Becas Desarrollo Sotenible'\n")

str(input("Ingrese porfavor el nombre del postulante a la beca\n"))

etnia= str(input("Ingrese porfavor la etnia del postulante. Elija entre:\n"  " 1. sin reconocimiento\n 2. afrodescendiente\n 3. indigena\n 4. raizal\n 5. palenquero\n 6. gitano\n" ))
estrato= int(input("Ingrese porfavor el estrato socioeconomico del postulante. Elija entre los siguientes estratos:\n"  " 1. 1\n 2. 2\n 3. 3\n 4. 4\n 5. 5\n 6. 6\n"))
ingreso= int(input("Ingrese porfavor el ingreso economico mensual del nucleo familiar del postulante. Elija enter las siguientes opciones:\n"  " 1. 0 - 908525\n 2. 908526\n 3. 1817052 - 2725578\n 4. 3634104\n 5. 4542630\n"))



if etnia == "sin reconocimiento":
    score1= 0
elif etnia == "afrodescendiente":
    score1= 8
elif etnia == "indigena":
    score1= 10
elif etnia == "raizal":
    score1= 12
elif etnia == "palenquero":
    score1= 14
elif etnia == "gitano":
    score1= 16
else:
    print("Se presento un error")
    
    
if estrato == 1:
    score2= 20
elif estrato == 2:
    score2= 16
elif estrato == 3:
    score2= 12
elif estrato == 4:
    score2= 8
elif estrato == 5:
    score2= 0
elif estrato == 6:
    score2= 0
else:
    print("Se presento un error")
    

if ingreso >= 0 or ingreso < 908526:
    score3= 30
elif ingreso == 908526:
    score3= 18
elif ingreso >= 1817052 or ingreso <= 272557:
    score3= 14
elif ingreso == 3634104:
    score3= 8
elif ingreso == 4542630:
    score3= 0
else:
    print("Se presento un error")

scoret= score1 + score2 + score3


if scoret >= 50:
    print("El candidato continua en el proceso de seleccion")
else:
    print("El candidato no continua en el proceso de seleccion")