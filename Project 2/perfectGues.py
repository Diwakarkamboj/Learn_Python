import random

class perfectGuess:  

    guesses = 0

    @staticmethod
    def numGenerator():
        compNum = random.randint(1, 100)
        # print(compNum)
        return compNum 
    
    def askUserNum(self):
        userInp = int(input("Please enter your guess number : "))
        return userInp

    def  checkGuess(self, userInp, compNum):
        while(True):
            self.guesses += 1
            if(userInp > compNum):
                print("Your guess is too high, Lower number please.")
            elif(userInp < compNum):
                print("Your guess is too low, Higher number please,")
            elif(userInp == compNum):
                print("You guessed it, You are a perfect guesser!")
                print(f"Number of gusses by user : {self.guesses}")
                break
            else:
                print("Invalid Input")
            
            userInp = self.askUserNum()


obj1 =  perfectGuess()
compNum = obj1.numGenerator()
userInp = obj1.askUserNum()
obj1.checkGuess(userInp, compNum)







