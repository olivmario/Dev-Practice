import random

def selectRandom(stream):
    result = None
    i = 0
    for value in stream:
        i += 1
        if random.randrange(i) == 0:
            result = value
    return result
