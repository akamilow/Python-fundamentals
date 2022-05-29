numbers = [2, 3, 5, 10, 20]

#Pythonic way 
doubledNumbers = [x * 2 for x in numbers]
print(doubledNumbers)
print('------------------------')

# Non-Pythonic way 
#Hacen tareas diferentes 
doubled_numbers = []
for i in range (len(numbers)):
     doubled_numbers.append (numbers[i] * 2)
     print(doubled_numbers)
print('------------------------')

#This is useful when u want to create a simple sequence of nums starting at zero
nums = range(0,11) #rage(start,stop)
nums_list = list (nums)
print (nums_list)
print('------------------------')

# range (stop) una lista del 0 al 10 el 11 no cuenta
nums = range(11)
nums_list = list (nums)
print (nums_list)
print('------------------------')

# range() de dos en dos hasta el 20 el 21 no cuenta
nums = range (2, 21, 2)
nums_list = list (nums)
print (nums_list)
print('------------------------')

#enumerate() enumerar los elementos de las listas 
letters = ['a', 'b', 'c', 'd' ] 
indexed_letters = enumerate(letters)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)
print('------------------------')

#enumerate(star) enumerar los elementos de las listas / empezando desde el num 5
letters = ['a', 'b', 'c', 'd' ] 
indexed_letters = enumerate(letters, start = 5)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)
print('------------------------')

#map() redondear numeros / function to apply a function to every element of an object
nums = [1.5, 2.3, 3.4, 4.6, 5.0] 
rnd_nums = map(round, nums)
print(list(rnd_nums))
print('------------------------')

#map() with lambda exponenciar whitout a loop 
nums = [1, 2, 3, 4, 5]  
sqrd_nums = map(lambda x: x ** 2, nums)
print(list(sqrd_nums))
print('------------------------')

