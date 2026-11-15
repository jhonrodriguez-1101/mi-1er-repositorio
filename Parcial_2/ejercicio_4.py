notas = { 
"Harry": [3.8, 4.0, 4.2], 
"Ron": [3.2, 3.8, 2.8], 
"Hemione": [5.0, 5.0, 5.0], 
"Draco": [4.5, 4.2, 5.0],
"Nevil": [2.5, 3.0, 3.2] 
} 
def promedio_notas(notas):
    for estudiante in notas:
        promedio = sum(notas[estudiante]) / len(notas[estudiante])
        print("El promedio de notas de", estudiante, "es:", promedio)
def promedio_ponderado(notas):
    for estudiante in notas:
        promedio = (notas[estudiante][0] * 0.3) + (notas[estudiante][1] * 0.3) + (notas[estudiante][2] * 0.4)
        print("El promedio ponderado de notas de", estudiante, "es:", promedio)
def mayor_promedio(notas):
    for estudiante in notas:
        promedio = sum(notas[estudiante]) / len(notas[estudiante])
        mas_alto = max(promedio)
        if promedio == mas_alto:
            print("El estudiante con el mayor promedio es:", estudiante, "con un promedio de:", promedio)
def estudiantes_apronbados(notas):
    for estudiantes in notas:
        promedio = sum(notas[estudiantes]) / len(notas[estudiantes])
        if promedio >= 3.0:
            print("El estudiante", estudiantes, "aprobo la clase de la profesora Macgonagall:", promedio)
        else:
            print("El estudiante", estudiantes, "no aprobo la clase de la profesora Macgonagall:", promedio)

encender_programa = print("Desea usar el programa de notas de la clase de la profesora Macgonagall? (SI o NO)")
encender = input("Respuesta: ")
encender = encender.upper()
while encender == "SI":
    print("Que desea hacer? ver el promedio de notas, ver el promedio ponderado, ver el mayor promedio o ver los estudiantes aprobados?")
    respuesta = input("Respuesta: ")
    respuesta = respuesta.lower()
    if respuesta == "ver el promedio de notas":
        promedio_notas(notas)
    elif respuesta == "ver el promedio ponderado":
        promedio_ponderado(notas)
    elif respuesta == "ver el mayor promedio":
        mayor_promedio(notas)
    elif respuesta == "ver los estudiantes aprobados":
        estudiantes_apronbados(notas)
    encender_programa = print("Desea ver algo mas de el programa de notas de la clase de la profesora Macgonagall? (SI o NO)")
    encender = input("Respuesta: ")
    encender = encender.upper()
else:
    print("Gracias por usar el programa de notas de la clase de la profesora Macgonagall, esperamos que haya sido de su agrado.")

