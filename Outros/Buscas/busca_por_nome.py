import sys
lista_exe = list(map(int, sys.stdin.readline().split()))
numero = int(sys.stdin.readline())

def buscar_por_nome(lista, nome):
    for matricula, nome_aluno in lista:
        if nome_aluno == nome:
            return matricula

    return None