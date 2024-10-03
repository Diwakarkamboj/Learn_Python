from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo


    def bookTick(self, fromStation, toStation):
        print(f"Your train no. {self.trainNo} is booked from {fromStation} to {toStation}")

    def getStatus(self):
        if(self.trainNo == 121):
            print(f"Train is running on Time, extra seats available {randint(1,10)}")
        else:
            print("Train is late")

    def getFare(self,fromStation, toStation):
        
        print(f"Your fare for train no. {self.trainNo} from {fromStation} to  {toStation} is {randint(1222, 1555)}")


obj1 = Train(121)
obj1.bookTick("Delhi", "Mumbai")
obj1.getFare("Delhi", "Mumbai")
obj1.getStatus()
