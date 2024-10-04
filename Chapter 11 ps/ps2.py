class Animal:
    print("I'm animal class")

class Pets(Animal):
    print("I'm a pet class")

class Dog(Pets):
    def bark(self):
        print("From Dog class dog says: Woof!")


obj = Dog()
obj.bark()  # Outputs: Woof!