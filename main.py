print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('You are at a cross road. Where do you want to go?')

left_or_right=str(input('Type \"left" or  "right" :')).lower()
if left_or_right == 'right':
    print('You take the path on the right. Unaware of the pitfall, you step on loose soil and fall into a hole. Game Over.')
else:
    print('You follow the left path until you reach the edge of a dark, wide lake.')
    wait_swim=str(input('Type \"wait" or "swim" :  ')).lower()
    if wait_swim == 'swim':
        print('Impatient, you dive into the water to swim across. Suddenly, a giant trout emerges from the deep. Attacked by trout. Game Over.')
    else:
        print('You choose to wait patiently at the shore until a safe passage appears. On the other side, you find an ancient structure with three colored doors.')
        door=str(input('Type ' + '\33[1;31mred door\33[m ' + 'or ' + '\33[1;34mblue door\33[m ' + 'or ' + '\33[1;33myellow door\33[m : ')).lower()
        if door == 'red door':
            print('You open the red door and an inferno engulfs the room. Burned by fire. Game Over.')
        elif door == 'blue door':
            print('You open the blue door into a dark chamber full of hungry creatures. Eaten by beasts. Game Over.')
        elif door == 'yellow door':
            print('You open the yellow door. The room opens up to reveal the chest full of legendary gold. You Win!')
        else:
             print('Action invalid. Game Over.')
