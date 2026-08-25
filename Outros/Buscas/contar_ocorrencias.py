import sys
lista_exe = list(map(int, sys.stdin.readline().split()))
numero = int(sys.stdin.readline())

def contar_ocorrencias(lista, x):
    ocorrencia = 0
    for i in range(len(lista)):
        if x == lista[i]:
            ocorrencia+=1
    return ocorrencia