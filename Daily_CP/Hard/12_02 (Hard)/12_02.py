def maior_soma_nao_adjacente(lista):
    anterior2 = 0
    anterior = 0

    for numero in lista:
        nova_soma = max(anterior2 + numero, anterior)
        
        anterior2 = anterior
        anterior = nova_soma
        
    return anterior

lista1 = [2, 4, 6, 2, 5]
lista2 = [5, 1, 1, 5]
lista3 = [1, 2, 3]
