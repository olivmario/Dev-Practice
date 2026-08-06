def busca_linear(lista, x):

    for i in range(len(lista)):
        if lista[i] == x:
            return ("indice da lista:", i)

    return -1

listaa = [2, 3, 12, 3, 15, 5, 54]
e = 15

print(busca_linear(listaa, e))


def busca_binaria(lista, x):
    inicio = 0
    fim = (len(lista) +1)
    for i in range(len(lista)):
