print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[GauravK]
*******************************************************************************''')
print("Welcome to the treasure island!.\n"
      "You're at a cross road."
      " Where do you want to go?"
      "\nYour mission is to find the treasure.\n")
direction=input("left or right? ")
# asking user direction left or right:
if direction =="right"or direction=="Right":#
    print("you fell into the hole.\nGame Over!")
elif direction =="left"or direction=="Left":
    print("You've come to a lake there is a island in the "
          "middle of the lake.\nwould you like to \"wait\" "
          "for a boat or \"swim\"")

    choice=input("swim or wait?")
    if choice =="swim" or choice =="Swim":
        print("Attacked by shark!\nGame Over!")
    elif choice =="wait" or choice =="Wait":
        choice=input("which door red, yellow, or blue")
        if choice=="red" or choice=="Red":
            print("Burned by fire.\nGame Over!")
        elif choice=="blue" or choice=="Blue":
            print("Eaten by beasts.\nGame Over!")
        elif choice=="yellow" or choice=="Yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
