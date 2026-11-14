"""Calculadora"""
def suma(a,b):
    return a + b 
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return "Error"
    dividir = a / b
    return dividir
def potencia(base,exponente):
    if exponente == 0:
        return 1
    veces = exponente
    resultado = base
    for numero in range(1,exponente):
        resultado = multiplicacion(resultado,base)
        veces -= 1
    return resultado
def raiz_cuadrada(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    if numero < 0:
        return "Error"
    base = numero
    for base in range(1,base):
        if multiplicacion(base,base) == numero:
            return base
    if multiplicacion(base,base) != numero:
        return "No tiene raiz cuadrada exacta"
    
def factorial(numero):
    if numero == 0:
        return 1
    resultado = numero
    for numero in range(1,numero):
        resultado = multiplicacion(resultado,numero)
    return resultado
def inversa(numero):
    if numero == 0:
        return "Error"
    inverso = 1/numero
    return inverso
print("Que quieres hacer?: SUMAR, RESTAR, MULTIPLICAR, DIVIDIR, POTENCIA, RAIZ CUADRADA, FACTORIAL, INVERSA")
operacion = input("Ingrese la operacion que desea realizar: ")
operacion = operacion.upper()
if operacion == "SUMAR":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    print(suma(a,b))
elif operacion == "RESTAR":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    print(resta(a,b))
elif operacion == "MULTIPLICAR":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    print(multiplicacion(a,b))
elif operacion == "DIVIDIR":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    print(division(a,b))
elif operacion == "POTENCIA":
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(potencia(base,exponente))
elif operacion == "RAIZ CUADRADA":
    numero = int(input("Ingrese el numero: "))
    print(raiz_cuadrada(numero))
elif operacion == "FACTORIAL":
    numero = int(input("Ingrese el numero: "))
    print(factorial(numero))
elif operacion == "INVERSA":
    numero = float(input("Ingrese el numero: "))
    print(inversa(numero))


