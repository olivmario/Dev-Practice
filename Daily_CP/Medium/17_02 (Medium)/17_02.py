import random

def Pi(n):
    inside = 0
    for i in range(n):
        x = -1 + 2 * random.random()
        y = -1 + 2 * random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / n

n = 100
print(Pi(n))
