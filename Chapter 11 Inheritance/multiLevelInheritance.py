class Employee:
    def e(self):
        print("Hey I'm an  employee")

class Programmer(Employee):
    def p(self):
        print("Hey I'm a programmer")

class programmerManager(Programmer):
    def c(self):
        print("Hey I'm a programmer Manager")


obj = programmerManager()
obj.e()
obj.p()
obj.c()

