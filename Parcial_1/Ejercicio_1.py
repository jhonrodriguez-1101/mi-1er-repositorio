Menu = {

    "Hamburguesa" : 16900,
    "Perro Caliente" : 18900,
    "Salchipapa" : 21900,
    "Pizza" : 8900,
    "Helado" : 10900,
    "Gaseosa" : 3500

}
Acumulado_pedido = 0
for comida, precio in Menu.items():
    print(comida, precio)
pedido = input("Deseas hacer un pedido: SI o NO: ")
while pedido == "SI":
    pedido_cliente = input("Que deseas pedir del Menu: ")
    if pedido_cliente in Menu:
        precio_pedido = Menu[pedido_cliente]
        Acumulado_pedido = Acumulado_pedido + precio_pedido
        print("El precio es: ", precio_pedido)
    else: 
        print("Tu pedido no esta en nuestro Menu piensa bien lo que quieres")
    pedido = input("Deseas hacer un pedido: SI o NO: ")
else:
    print("Gracias por su visita")
if Acumulado_pedido > 0:
    print("Tienes que paggar: $",Acumulado_pedido)

