palabra_del_usuario = input("Ingrese Palabra: ")
tamaño = len(palabra_del_usuario)
for tamaño in range(0, tamaño + 1):
    for inicio in range(0, tamaño + 1):
        fin = inicio + tamaño
        print (palabra_del_usuario[inicio:fin])