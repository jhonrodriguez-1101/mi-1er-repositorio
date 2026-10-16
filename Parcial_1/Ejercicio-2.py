entrar = input("¿Quieres jugar: SI o NO: ")
acumulado = 0
while entrar == "SI":
    edad = int(input("¿Cual es tu edad?: ")) 
    if edad < 5:
        entrada = 0
        total = entrada + acumulado
        acumulado = total
        print("Entras gratis")
    elif edad >= 5 and edad <= 18:
        entrada = 5
        total = acumulado + entrada
        acumulado = total
        print ("Tu entrada cuesta 5")
    elif edad > 18:
        entrada = 10
        total = acumulado + entrada
        acumulado = total
        print ("Tu entrada cuesta 10")
    print ("Debes pagar: $",acumulado)
    entrar = input("¿Quieres jugar: SI o NO: ")
if entrar == "NO":
    print ("Vuelve pronto")
        
