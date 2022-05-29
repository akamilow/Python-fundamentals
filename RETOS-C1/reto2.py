#DEFINICIÓN DE VARIABLES
nestor = input().upper()
pedro = input().upper()
jurado = input().upper()

ventaja_nestor = 0
ventaja_pedro = 0

for i in jurado:
    #SISTEMA DE PUNTOS
    if i in nestor:
        ventaja_nestor += 1
    if i in pedro:
        ventaja_pedro += 1
    #VALIDACIONES
    if (ventaja_pedro > ventaja_nestor):
        print("K", end="")
    elif (ventaja_pedro < ventaja_nestor):
        print("J", end="")
    else: 
        print("L", end="")