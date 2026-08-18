import sys

array = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

c = {}

for i in range(len(array) - x + 1):
    subar = array[i:i + x]

    for num in set(subar):
        c[num] = c.get(num, 0) + 1

maior = -1

for num in c:
    if c[num] == 1:
        maior = max(maior, num)

print(maior)       

    

