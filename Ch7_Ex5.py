#Умножение чисел двух списков с помощью for
NumOne=[8, 19, 148, 4]
NumTwo=[9, 1, 33, 83]
NumRes=[]

for i in NumOne:
    for j in NumTwo:
        NumRes.append(i*j)
print(NumRes)
