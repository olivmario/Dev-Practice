List = [1, 2, 3, 4, 5]
ListCalc = []

for i in range(len(List)):
    resul = 1
    for y in range(len(List)):
        if i != y:
            resul = resul * List[y]
    ListCalc.append(resul)


print(List)
print(ListCalc)