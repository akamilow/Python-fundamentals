"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
""" Manera no optimizada...
def array_front9(nums):
  shortesNums = nums[:4]
  if len(nums) < 4:
    for i in nums:
      if i == 9:
        return True
    return False
  else:
    for i in shortesNums:
      if i == 9:
        return True
    return False
"""

def array_front9(nums):
  # Recortamos el array para obtener los primeros 4 numeros.
  # para esto verificamos la longitud del array, si el contenido tiene mas de 4 numeros asigna la variable "end" que sea igual a 4 para el recorte.
  end = len(nums) 
  if end > 4: 
    end = 4
  
  for i in range(end):  # loop sobre index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False

print(array_front9([1, 2, 3, 9]))