import random 

def pc_guess(x):
    lowest_number = 1
    highest_number = x
    feedback = ""

    while feedback != "C":
        if lowest_number != highest_number:
            guess = random.randint(lowest_number, highest_number)
        else:
            guess = lowest_number #could also be highest_number / low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?: ->").upper()
        if feedback == "H":
            highest_number = guess - 1
        elif feedback == "L":
            lowest_number = guess + 1

    print("--------------------------------------------------")
    print(f"The pc guessed your number, {guess}, correctly!!")

# function call
pc_guess(10)
