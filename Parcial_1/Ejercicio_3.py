bolsa = int(input("¿Cuantas bolsas hay: "))
total_bolsas = bolsa
for n in range(bolsa):
    print ("Hay bolsas")
    print("Vaciar arroz")
    vaciar_arroz = input("¿Se vacio el arroz correctamente?: SI o NO: ")
    if vaciar_arroz == "SI":
        total_bolsas = bolsa - 1
        print("La bolsa tiene arroz")
        print("Sellar bolsa")
        sellar_bolsa = input("¿La bolsa se sello correctamente?: SI o NO: ")
        if sellar_bolsa == "SI":
            total_bolsas = total_bolsas - 1
            print("Bolsa sellada, lista para empacar")
        elif sellar_bolsa == "NO":
                    print("Hubo un fallo")
    elif vaciar_arroz == "NO":
        print("Hubo un fallo")
if total_bolsas < 1:
    print("No hay bolsa, porfavor ingresar bolsa")