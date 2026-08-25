import sys
lista_exe = list(map(int, sys.stdin.readline().split()))
numero = int(sys.stdin.readline())


def busca_linear(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return i
        
    return -1

##print(busca_linear(lista_exe, numero))

#Para listas ordenadas
def busca_binaria(lista, x):
    ini = 0
    fim = len(lista) - 1

    while ini <= fim:
        meio =(ini + fim) // 2
        if lista[meio] == x:
            return meio
        elif x>lista[meio]:
            ini = meio +1
        else:
            fim = meio- 1

    return -1

print(busca_binaria(lista_exe, numero))