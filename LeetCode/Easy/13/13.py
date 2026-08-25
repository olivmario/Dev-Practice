import sys

s = sys.stdin.readline().strip()

valores = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

resultado = 0

for i in range(len(s)):
    atual = valores[s[i]]

    if i + 1 < len(s) and atual < valores[s[i + 1]]:
        resultado -= atual
    else:
        resultado += atual

sys.stdout.write(str(resultado))