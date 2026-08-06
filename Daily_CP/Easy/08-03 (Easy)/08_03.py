lista = [2, 1, 5, 7, 2, 0, 5]


def cont(lista):

    lista.sort()

    n = len(lista)//2
    if len(lista) % 2 == 0:
        median = (lista[n-1] + lista[n])
        return median/2
    else:
        median = lista[n]
        return median

print (cont(lista))