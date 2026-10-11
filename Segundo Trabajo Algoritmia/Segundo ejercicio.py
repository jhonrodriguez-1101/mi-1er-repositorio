lista = [2,4,3,1,6,7,5,8,9,10]
for j in range(len(lista)):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            lista [i], lista [i+1] = lista [i+1], lista [i]
            print (lista)
