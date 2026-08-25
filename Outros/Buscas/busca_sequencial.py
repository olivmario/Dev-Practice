import random
import time
import matplotlib.pyplot as plt


def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


tamanhos = [1000, 5000, 10000, 20000]
tempos = []

for n in tamanhos:

    lista = random.sample(range(100000), n)

    alvo = lista[-1]

    inicio = time.time()

    busca_sequencial(lista, alvo)

    fim = time.time()

    tempo = fim - inicio
    tempos.append(tempo)

    print(f"n = {n} | tempo = {tempo:.8f} segundos")


plt.plot(tamanhos, tempos, marker='o')

plt.xlabel("Tamanho do Vetor (n)")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Busca Sequencial")

plt.grid()
plt.show()