class Complex:

    def __init__(self,r,i):
        self.r = r
        self.i = i
        
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        return  Complex(((self.r * c2.r) - self.i * c2.i), ((self.r * c2.i) + (self.i * c2.r)))

    
    def __str__(self):
        return  f"{self.r} + {self.i}i"


obj1 = Complex(1, 2)
obj2 = Complex(3, 4)
print(obj1 + obj2)
print(obj1 * obj2)


