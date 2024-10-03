''' 
We all have played snake, water gun game in our childhood. If you haven’t, 
google the rules of this game and write a python program capable of playing this 
game with the user.

1 for snake  b=1 and u=1, b=1 and u=-1, b=1 and u=0
-1 for water b=-1 and u=-1, b=-1 and u=1, b=-1 and u=0
0 for gun    b=0 and u=0, b=0 and u=-1, b=0 and u=1
''' 

import random

gameOptions = {"s":"snake","w":"water", "g":"gun"}
print(gameOptions)

user_input = input("Choose your option from above given that: 's' for snake, 'w' for water, 'g' for gun: ")

bot = random.choice([-1,0,1])

dict = {"s" : 1,  "w" : -1, "g" : 0}
revDict = {1: "Snake", -1 : "Water", 0 : "Gun"}

if user_input not in dict:
    print("Invalid input")
else:
    youNum = dict[user_input]

print(f"You choose  {revDict[youNum]} \nBot choose {revDict[bot]}")

#result
if(bot == youNum):
    print("It's a tie!")
else:
    if(bot == 1 and youNum == -1): #or \
        print("You lose")
    elif(bot == -1 and  youNum == 0):
        print("You lose")
    elif(bot == 0 and  youNum == 1):
        print("You lose")
    # elif(bot == 1 and  youNum == 0):
    #     print("You win")
    # elif(bot == -1 and youNum == 1):
    #     print("You win")
    # elif(bot == 0 and youNum == -1):
    #     print("You win")
    else:
        print("You win")
    
    