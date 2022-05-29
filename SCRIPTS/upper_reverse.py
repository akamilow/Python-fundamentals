
# uppercase_and_reverse("Do not go gentle into that good night.")
# "THGIN DOOG TAHT OTNI ELTNEG OG TON OD"

def uppercase_and_reverse(text):
    uppercasetext = text.upper()
    reversedtext = uppercasetext[::-1]
    return reversedtext

print(uppercase_and_reverse("camilo"))

#--------------------------------------

def uppercase_and_reverse(text):
    return text.upper()[::-1]
    
print(uppercase_and_reverse("banana"))

#---------------------------------------
    
def reverse(text):
    return text[::-1]

print(reverse("castellar"))