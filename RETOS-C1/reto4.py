import json

dic = json.loads(input())

llaves_lista = input().split()

dic_lista = []
lista_suma = []

for key in dic.keys():
    dic_lista.append(key)

for i in llaves_lista:
    for j in dic_lista:
        if(i==j):
            lista_suma.append(i)

contador = 0
for letra in lista_suma:
    for llave,valor in dic.items():
        if letra == llave: 
            contador += valor

print(contador)       
print(*lista_suma)