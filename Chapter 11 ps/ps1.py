class twoDVector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x}i, {self.y}j")

class threeDVector(twoDVector):

    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z = z
        
    def show2(self):
        print(f"{self.x}i, {self.y}j, {self.z}k")


obj1 = threeDVector(1,2,3)
obj1.show()
obj1.show2() 


