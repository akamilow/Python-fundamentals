'''
Al preguntarle al tendero el precio de los huevos y la leche me responde que si le quito 4 pesos al precio de la leche obtengo dos veces 
el precio de los huevos y si sumo el precio de la leche y los huevos me da cinco veces el precio del café. 
Adicionalmente, todos los productos fueron gravados con diferentes porcentajes basados en las siguientes categorías:

- Categoría uno: para productos que valgan entre 0 y 20 pesos
- Categoría dos: para productos entre 21 y 30 pesos
- Categoría tres: para productos entre 31 y 50 pesos
- Categoría cuatro: para productos que valgan más de 50 pesos.

Dado el precio de los huevos, realizar un programa que imprima en la primera línea los precios de los huevos, 
la leche y el café separados por un solo espacio. En la segunda línea indique con qué categoría fue grabado el café.
'''

precio_huevos = int(input('Cual es el precio de los huevos? ->'))

precio_leche = 2 * precio_huevos + 4

precio_cafe = int(precio_huevos + precio_leche) // 5

print(f'{precio_huevos} {precio_leche} {precio_cafe}')

if (precio_cafe > 0 and precio_cafe < 20): 
    print('uno')
elif (precio_cafe >= 21 and precio_cafe < 30):
    print('dos')
elif (precio_cafe > 31 and precio_cafe < 50):
    print('tres')
else:
    print('cuatro')

