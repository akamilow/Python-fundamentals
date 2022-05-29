apuesta = input().upper().split(",")

letras = []
letra_repetidas = ""

numeros = []
contador = 0

for i in range(len(apuesta)):
    if letra_repetidas != apuesta[i]: 
        letra_repetidas = apuesta[i]
        letras.append(letra_repetidas) 

    if apuesta[0] != apuesta[i]:
        apuesta[0] = apuesta[i]
        numeros.append(contador) 
        contador = 0

    if apuesta[0] == apuesta[i]: 
        contador += 1

if contador != 0:
    numeros.append(contador)

for i in letras:
    print(i, end=" ")
print("\n")
for i in numeros:
    print(i, end=" ")