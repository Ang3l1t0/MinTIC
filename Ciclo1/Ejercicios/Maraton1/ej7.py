temperatura = float(input('Ingrese la temperatura en °C: '))
if temperatura <= 10 and temperatura < 10:
    sensacion_termica = 'Mucho frio'
elif temperatura >= 10 and temperatura < 15:
    sensacion_termica = 'Poco frio'
elif temperatura >= 15 and temperatura < 25:
    sensacion_termica = 'Temperatura normal'
elif temperatura >= 25 and temperatura < 30:
    sensacion_termica = 'Poco calor'
elif temperatura >= 30 and temperatura < 40:
    sensacion_termica = 'Mucho calor'
else:
    sensacion_termica = 'Temperatura fuera de rango'
print(sensacion_termica)
