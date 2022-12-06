"""
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

# def front_back(str):
#     str_list = list(str)
#     first_char = str_list[0]
#     last_char = str_list[len(str_list) - 1]

#     if len(str) <= 1:
#         return str

#     str_list.pop(0)
#     str_list.pop(len(str_list) - 1)

#     return last_char + "".join(str_list) + first_char

def front_back(str):
    if len(str) <= 1:
      return str

    mid = str[1:len(str)-1]
    
    return str[len(str)-1] + mid + str[0]
    

print(front_back('code'))
