import random 

def play():
    user = input("What's your choice?'R' for Rock, 'P' for paper, 'S' for scissors: ->").upper()
    pc = random.choice(['R', 'P', 'S'])

    if user == pc:
        return 'It\'s a tie'
    
    # R > S, S > P, P > R
    if is_win(user, pc):
        return 'YOU WON!'
    
    return 'YOU LOST!'

def is_win(player, opponent):
    # return True or False
    # R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True

print(play())