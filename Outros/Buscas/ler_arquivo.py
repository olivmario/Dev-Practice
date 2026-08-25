lista = []
with open("dados_busca.txt", "r") as dados:
    for linha in dados:
        lista.append(int(linha))

def busca_sequencial(lista, x):
    for i in range(len(lista)):
        if x == lista[i]:
            return f"numero {x} encontrado na linha {i+1}"

print(busca_sequencial(lista, 5))