#The game() function in a program lets a user play a game and 
# returns the score as an integer. You need to read a file ‘Hi-score.txt’ 
# which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever 
# the game() function breaks the Hi-score.

def game(a,b):
    c = a + b
    return c

sum = game(10,9)
# print(sum)

with open("Hi-score.txt") as e:
    data = e.read()
    if(sum >  int(data)):
        with open("Hi-score.txt", "w") as  f:
            f.write(str(sum))
    print(f"Previous high-score was {data}")
    print(f"Your score is {sum}")
    


