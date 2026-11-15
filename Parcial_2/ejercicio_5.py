def elegir_dificultad():
    print("¿Que dificultad desea elegir? facil, medio o dificil?")
    dificultad = input("Respuesta: ")
    dificultad = dificultad.lower()
    if dificultad == "facil":
        return 10
    elif dificultad == "medio":
        return 6
    elif dificultad == "dificil":
        return 3
    else:
        print("No existe esa dificultad, por favor elija entre facil, medio o dificil.")
    return 
def generar_numero():
    import random
    numero = random.randint(1, 100)
    print("El numero generado es:", numero)
    return numero
    print("El numero generado es:", numero)
def numero_intentos (elegir_dificultad, generar_numero):
    if elegir_dificultad > 0:
        print("¿Desea hacer un intento?")
        respuesta = input("SI o NO: ")
        respuesta = respuesta.upper()
        while respuesta == "SI":
            elegir_dificultad = elegir_dificultad -1
            print("Ingrese su numero del 1 al 100")
            numero = int(input("Numero es: "))
            numero_aleatorio = generar_numero
            if numero == numero_aleatorio:
                print("Felicitaciones adivinaste el numero eres el mejor")
                return
            else:
                print("Intentalo de nuevo, ¿quieres una pista?")
                pista = input("SI o NO: ")
                pista = pista.upper()
                if pista == "SI":
                    if numero > numero_aleatorio:
                        print("La frecuencia es un poco mas baja")
                    if numero < numero_aleatorio:
                        print("La frecuencia es un poco mas alta")
                else:
                    print("Sigue intentando")
            if elegir_dificultad > 0:
                print("¿Desea hacer un intento?")
                respuesta = input("SI o NO: ")
                respuesta = respuesta.upper()
            else:
                print("Perdiste gracias por jugar")
                return
        else:
            print("Gracias por jugar")

encender = print("¿Desea jugar? SI o NO")
respuesta = input("SI o NO: ")
respuesta = respuesta.upper()
while respuesta == "SI":
    print("Primero elige la dificultad")
    dificultad = elegir_dificultad()
    numero_alea = generar_numero()
    intentos = numero_intentos(dificultad, numero_alea)
    encender = print("¿Desea volver jugar? SI o NO: ")
    respuesta = input("SI o NO: ")
    respuesta = respuesta.upper()
else:
    print("Gracias por su visita")


