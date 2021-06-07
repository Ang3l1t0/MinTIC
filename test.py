from operator import itemgetter


def count_element(lista):
    cuenta = 0
    lista1 = []
    for i in lista:
        cuenta = lista.count(i)
        if i == '1':
            #sinreconocimiento += 1
            sr = ('sin reconocimiento', 1, cuenta)
            lista1.append(sr)
        elif i == '2':
            ad = ('afrodescendiente', 2, cuenta)
            lista1.append(ad)
        elif i == '3':
            ig = ('indigena', 3, cuenta)
            lista1.append(ig)
        elif i == '4':
            rz = ('raizal', 4, cuenta)
            lista1.append(rz)
        elif i == '5':
            pq = ('palenquero', 5, cuenta)
            lista1.append(pq)
        elif i == '6':
            gt = ('gitano', 6, cuenta)
            lista1.append(gt)
    etnia = sorted(lista1, key=itemgetter(2, 1))
    print(etnia[0][0])


day3 = ['6', '5', '3', '3']
count_element(day3)
