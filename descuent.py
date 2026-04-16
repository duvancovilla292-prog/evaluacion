det = 0
def dest():
    global det
    det = 0
    if input("¿Desea aplicar descuento? (s/n): ").lower() == 's':
        while True:
            det=int(input("Ingrese el descuento (0-50): "))
            if det >= 0 and det <= 50:
                print ("el porcentaje es correcto ")
                break
            else:
                print("porcentaje invalido ")
    return det
    