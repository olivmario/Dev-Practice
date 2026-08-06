Lista = [2, 1, 2]
NewList = []


left = 0
right = 0
water = 0

for i in range(1, len(Lista)):

    for j in range(i):
        left = max(left, Lista[j])

    for r in range(i, len(Lista)):
        right = max(right, Lista[r])

    waterd = min(left, right) - Lista[i]
    water += waterd

print(water)