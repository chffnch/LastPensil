import random

# bot strategy
def bot_move(pencils_num):
    move = 0
    
    # determine if bot is in a winning position
    if pencils_num % 4 == 0 or pencils_num % 4 == 3 or pencils_num % 4 == 2:
        winning = True
    else:
        winning = False
    
    # strategy for being in a winning position
    if winning:
        if pencils_num % 4 == 0:
            move = 3
        elif pencils_num % 4 == 3:
            move = 2
        else:
            move = 1
        
    # strategy for not being in a winning position
    else:
        if pencils_num == 1:
            move = 1
        else:
            move = random.randint(1, 3)
                
    return move


# 01. Game setup

# Input validity check: pencils number
while True:
    try:
        pencils_num = int(input("How many pencils would you like to use:"))
    except ValueError:
        print("The number of pencils should be numeric") 
        continue
    
    if pencils_num <= 0:
        print("The number of pencils should be positive")
        continue
    else:
        break

players = ["player", "bot"]

# Input validity check: first player
while True:
    current_player = input(f"Who will be the first ({players[0]}, {players[1]}):")
    if current_player not in players:
        print(f"Choose between {players[0]} and {players[1]}")
        continue
    else:
        i = players.index(current_player)
        break
    
# 02. Game process

print("|" * pencils_num)

while pencils_num > 0:
    print(f"{current_player}'s turn:")
    while True:    
        try:
            if i == 1: # bot's move
                pencils_taken = bot_move(pencils_num) 
                print(pencils_taken)
            else:
                pencils_taken = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
            continue
        
        if pencils_taken not in (1, 2, 3):
            print("Possible values: '1', '2' or '3'")
            continue
        
        if pencils_taken > pencils_num:
            print("Too many pencils were taken")
            continue
        else:
            pencils_num = pencils_num - pencils_taken
            print("|" * pencils_num)
            break
    
    # switch turn
    if i == 0:
        i = 1
    else:
        i = 0
    current_player = players[i]
    
print(f"The {current_player} won!")