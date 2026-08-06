import sys

def main():
    dados = sys.stdin.read().split()
    energia = int(dados[0])
    lista1 = []
    lista2 = []
    X = 0
    s = 0
    p = 0

    for i in range(int(dados[1])):
        lista1.append(int(dados[3+i]))

    for i in range(int(dados[2])):
        lista2.append(int(dados[3+len(lista1)+i]))

    for i in range(0, len(lista1)+len(lista2)):

        if len(lista1)>s and energia - int(lista1[s]) >=0:
            energia -= int(lista1[s])
            X+= 1
            s += 1
        elif len(lista2)>p:
                energia += int(lista2[p])
                X+=1
                p+=1
        
        else:
            break

    print(X)
        

if __name__ == "__main__":
    main()