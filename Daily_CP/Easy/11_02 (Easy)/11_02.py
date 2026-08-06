class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
def cont(raiz):
    def helper(no):
        if not no:
            return 0, True
        
        cont_esquer, esq = helper(no.esquerda)
        cont_direit, dir = helper(no.direita)
        
        total = cont_esquer + cont_direit

        if esq and dir:
            if no.esquerda and no.valor != no.esquerda.valor:
                return total, False
            if no.direita and no.valor != no.direita.valor:
                return total, False
            
            return total +1, False
        
        return total, False
    contar, _ = helper(raiz)
    return contar
    
raiz = No(0)

raiz.esquerda = No(1)
raiz.direita = No(0)

raiz.direita.esquerda = No(1)
raiz.direita.direita = No(0)

raiz.direita.esquerda.esquerda = No(1)
raiz.direita.esquerda.direita = No(1)

print(cont(raiz))





