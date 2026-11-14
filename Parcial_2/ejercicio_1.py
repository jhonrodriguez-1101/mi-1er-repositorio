lecturas_voltaje = [13380, 13410, 13450, 13440, 13400, 13350, 13280, 13210, 13190, 13200, 13220, 13210, 13180, 13190, 13220, 13250, 13230, 13150, 13000, 12950, 12980, 13050, 13150, 13280]
def calcular_promedio(lecturas):
    suma = sum(lecturas)
    promedio = suma / len(lecturas)
    return promedio
def altos_y_bajos(lecturas):
    maximo = max(lecturas)
    minimo = min(lecturas)
    return maximo, minimo
def horas_encima_promedio(lecturas, promedio):
    horas = 0
    for voltaje in lecturas:
        if voltaje > promedio:
            horas += 1
    return horas
print("El promedio de voltaje del dia es: ", calcular_promedio(lecturas_voltaje))
print("El voltaje maximo y el minimo del dia es: ", altos_y_bajos(lecturas_voltaje))
print("El numero de horas que el voltaje estuvo por encima del promedio es: ", horas_encima_promedio(lecturas_voltaje, calcular_promedio(lecturas_voltaje)))