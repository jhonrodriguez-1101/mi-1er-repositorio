"""Maquina Expendedora"""
producto = {

    "1" : ["chocolatina" , 1000],
    "2": ["gaseosa" , 3000],
    "3" : ["papas" , 2000],
    "4" : ["chicles" , 500],
    "5" : ["maduritos" , 3500]

}
def cobrar ():
    print("¿Desea un producto?")
    respuesta = input("SI o NO: ")
    respuesta = respuesta.upper()
    cuenta = 0 
    while respuesta == "SI":
        print("¿Que desea pedir): ", producto)
        pedido = input("Ingrese el numero de su producto: ")
        if pedido in producto:
            pedido = producto[pedido]
            comida = pedido[0]
            precio = pedido[1]
            print ("Tu pedido es: ", comida, "y su precio es: ", precio)
            cuenta = cuenta + precio
            print("Su precio total es: ", cuenta)
            print("¿Desea un producto?")
            respuesta = input("SI o NO: ")
            respuesta = respuesta.upper()   
        else: 
            print("No estas eligiendo entre las opciones dadas")
            print("¿Desea un producto?")
            respuesta = input("SI o NO: ")
            respuesta = respuesta.upper()
    else: 
        print("Gracias por su visita")
    return cuenta
def pago (cuenta):
    print("Debes pagar: ",cuenta)
    realizar_pago = int(input("Deposite: Solo billetes: "))
    if realizar_pago >= cuenta:
        pago = realizar_pago - cuenta
        print("Pago realizado con exito, su devuelta es: ",pago)
    else: 
        pago = cuenta - realizar_pago
        print("Error en el pago, Falta: ",cuenta)
        
    

print("¿Desea encender la maquina?: ")
encender_maquina = input("Encender ON, Apagar OFF: ")
encender_maquina = encender_maquina.upper()
while encender_maquina == "ON":
    total = cobrar ()
    pago(total)
    print("¿Desea encender la maquina?: ")
    encender_maquina = input("Encender ON, Apagar OFF: ")
    encender_maquina = encender_maquina.upper()
else:
    print("Hasta luego")    

