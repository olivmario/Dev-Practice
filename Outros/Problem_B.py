import sys


def main():
    dados = sys.stdin.read().split()

    N = int(dados[0])
    H = int(dados[1])
    vezes = 0

    A = list(map(int, dados[2:]))
    for i in range(N):
        if H >= A[i]:
            vezes+=1

    print(vezes)

if __name__ == "__main__":
    main()
            