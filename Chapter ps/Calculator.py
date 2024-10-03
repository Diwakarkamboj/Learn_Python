class Calculator:
    
    def __init__(self, num, operationType):
        self.num = num
        self.operationType = operationType

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def squareRoot(self):
        return self.num ** 0.5

    def calculate(self):
        if self.operationType == "square":
            return self.square()
        elif self.operationType == "cube":
            return self.cube()
        elif self.operationType == "squareroot":
            return self.squareRoot()
        else:
            return "Invalid Opeartion"

num = int(input("Enter a number: "))
operation = input("Enter which operation you want to perform: \"square\" \"cube\" \"squareroot\": ")

calc = Calculator(num, operation)

result = calc.calculate()
print(result)
        