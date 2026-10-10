
total_acumulado = 0.0
precio_base = 1.90
pedido_helado = input("¿Deseas pedir un helado? (SI o NO)")
if pedido_helado == "NO":
    print("Gracias por tu visita, vuelve pronto")
else:
    while pedido_helado == "SI":
        helado_con_toppings = input("¿quieres un topping? (SI o NO): ")
        if helado_con_toppings == "SI":
            print("¿Qué topping te gustaría agregar?")
            topping_elegido = input("elige un topping: Frutas, Granola, Oreo, Brownie: ")
            if topping_elegido == "Frutas":
                precio_topping = 0.50
                precio_total = precio_base + precio_topping
                total_acumulado += precio_total
                print("El precio total de tu helado es: $" + str(precio_total))
            elif topping_elegido == "Granola":
                precio_topping = 1.50
                precio_total = precio_base + precio_topping
                total_acumulado += precio_total
                print("El precio total de tu helado es: $" + str(precio_total))
            elif topping_elegido == "Oreo":
                precio_topping = 1.00
                precio_total = precio_base + precio_topping
                total_acumulado += precio_total
                print("El precio total de tu helado es: $" + str(precio_total))
            elif topping_elegido == "Brownie":
                precio_topping = 0.75
                precio_total = precio_base + precio_topping
                total_acumulado += precio_total
                print("El precio total de tu helado es: $" + str(precio_total))
            else:
                print("Ese topping no existe en el menú")
                precio_topping = 0
                precio_total = precio_base + precio_topping
                total_acumulado = precio_total + total_acumulado
                print("El precio total de tu helado es: $" + str(precio_total))
        elif helado_con_toppings == "NO":
                print("El precio total de tu helado es: $1.90")
        total_acumulado = total_acumulado + 1.90
        pedido_helado = input("¿Deseas pedir un helado? (SI o NO)")
        if pedido_helado == "NO":
            print("Gracias por tu visita, vuelve pronto")
if total_acumulado > 0:
    print("El valor total de tus helados comprados es: $" + str(total_acumulado))
