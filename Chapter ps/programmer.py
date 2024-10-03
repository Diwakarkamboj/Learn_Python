#Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__  (self, name, age, company):
        self.name = name
        self.age = age
        self.company = company


    @staticmethod
    def input_data_into_file():
        name = input("Please enter your name")
        age = int(input("Please enter your age"))
        with open("programmers.txt", "w") as file:
            file.write(f"Name: {name}\n Age: {age}\n Company:  {Programmer.company}\n")

    def input_self_data_into_file(self):
        with open("programmers.txt", "a") as file:
            file.write(f"Name: {self.name}\n Age: {self.age}\n Company:  {self.company}\n")


Programmer.input_data_into_file()
obj = Programmer("Rohan", 35,  Programmer.company)
obj1 = Programmer("Ram", 32,  "Apple")
obj.input_self_data_into_file()
obj1.input_self_data_into_file()


