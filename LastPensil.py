
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

players = ["John", "Jack"]

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
    
print(f"{current_player} won!")