"""
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

# Inicializamos la funcion
def array_count9(nums):
    # Inicializamos el contador
    count = 0

    # Realizaomos un bucle que recorra el array
    for i in nums:
        # Realizamos la condición que identifica si el array conetiene 9
        if i == 9:
            # Si la condición aplica el contador sube 1 por cada 9
            count+=1
    # Retornamos el contador
    return count

# Corremos funcion
print(array_count9([1, 2, 9, 9, 9, 3, 5, 9]))