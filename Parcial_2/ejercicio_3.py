"""Ejercicio 3"""
#Diccionairio muestra el nombre, su medida, la cantidad y el precio de cada componente
diccionario = {
    "resistencia": ["10k", 0, 200],
    "capacitor": ["100uF", 0, 1200],
    "inductor": ["1H", 0, 500],
    "frecuencia": ["60Hz", 0, 50],
    "potenciometro": ["5k", 0, 100],
}
#funcuion para calcular el precio total de los componentes en el diccionario, multiplicando la cantidad por el precio de cada componente
def precio_total(diccionario):
    total = 0
    for componente in diccionario:
        total += diccionario[componente][1] * diccionario[componente][2]
    return total
#fuincion para mostrar el diccionario, mostrando el nombre del componente, su medida, la cantidad y el precio
def mostrar_diccionario(diccionario):
    print("El diccionario contiene los siguientes componentes:", diccionario)
#funcion para agregar un componente al diccionario, si el componente ya existe, se le pregunta al usuario si desea aumentar la cantidad 
def agregar_componente(diccionario, nombre):
    if nombre in diccionario:
        print("El componente ya existe en el diccionario. ¿Desea aumentar la cantidad? (SI o NO)")
        respuesta = input("Respuesta: ")
        respuesta = respuesta.upper()
        if respuesta == "SI":
            print ("La cantidad actual de", nombre, "es:", diccionario[nombre][1])
            agregar = int(input("Ingrese la cantidad a agregar: "))
            cantidad = diccionario[nombre][1] + agregar
            diccionario[nombre][1] = cantidad
            print("La nueva cantidad de", nombre, "es:", cantidad)
            print(diccionario)
            return cantidad
        else:
            print("No se ha agregado nada.")
    else: 
        print("El componente no existe en el diccionario. ¿Desea agregarlo? (SI o NO)")
        respuesta = input("Respuesta: ")
        respuesta = respuesta.upper()
        if respuesta == "SI":
            nombre = input("Ingrese el nombre del componente: ")
            nombre = nombre.lower()
            medida = input("Ingrese la medida del componente: ")
            cantidad = int(input("Ingrese la cantidad del componente: "))
            precio = int(input("Ingrese el precio del componente: "))
            diccionario[nombre] = [medida, cantidad, precio]
            print("El componente ha sido agregado al diccionario.")
            print(diccionario)
        else:
            print("No se ha agregado nada.")
#funcion para eliminar un componente del diccionario, si el componente no existe, se le informa al usuario
def eliminar_componente(diccionario,nombre):
    if nombre in diccionario:
        print("El componente existe en el diccionario. ¿Desea eliminarlo? (SI o NO)")
        respuesta = input("Respuesta: ")
        respuesta = respuesta.upper()
        if respuesta == "SI":
            del diccionario[nombre]
            print("El componente ha sido eliminado del diccionario.")
            print(diccionario)
        else:
            print("No se ha eliminado nada.")
    else:
        print("No se elimino ningun componente, ya que el componente no existe en el diccionario.")

encender_programa = print("Desea encender el programa? (SI o NO)")
respuesta = input("Respuesta: ")
respuesta = respuesta.upper()
while respuesta == "SI":
    print("Que desesa hacer? agregar un componente, eliminar un componente, mostrar el diccionario o calcular el precio total?")
    respuesta = input("Respuesta: ")
    respuesta = respuesta.lower()
    if respuesta == "agregar un componente":
        print("Desea agregar un componente al diccionario? (SI o NO)")
        respuesta = input("Respuesta: ")
        respuesta = respuesta.upper()
        if respuesta == "SI":
            nombre = input("Ingrese el nombre del componente: ")
            nombre = nombre.lower()
            agregar_componente(diccionario, nombre)
            
    elif respuesta == "eliminar un componente":
        print("Desea eliminar un componente del diccionario? (SI o NO)")
        respuesta = input("Respuesta: ")
        respuesta = respuesta.upper()
        if respuesta == "SI":
            nombre = input("Ingrese el nombre del componente: ")
            nombre = nombre.lower()
            eliminar_componente(diccionario, nombre)  
    elif respuesta == "mostrar el diccionario":
        mostrar_diccionario(diccionario)
    elif respuesta == "calcular el precio total":
        print("El precio total de los componentes es: ", precio_total(diccionario))
    else:
        print("No se ha ingresado una opcion valida.")
    encender_programa = print("Desea encender el programa? (SI o NO)")
    respuesta = input("Respuesta: ")
    respuesta = respuesta.upper()
if respuesta == "NO":
    print("El programa ha sido apagado.")

