class Emp:
    name = "Ram"
    age = 25
    salary = 5000

    def __init__(self,name,age,salary): #dunder method auto called
        self.name = name
        self.age = age
        self.salary = salary
        print("I'm a constructor\n")
    
    def  display_instance_details(self):

        print("Instance method details:::")
        print("Employee Name: ", self.name)
        print("Employee  Age: ", self.age)
        print("Employee  Salary: ", self.salary, "\n")

    @staticmethod
    def  display_details():
        print("Static method details:::")
        print("Employee Name: ", Emp.name)
        print("Employee  Age: ", Emp.age)
        print(f"Employee  Salary:  {Emp.salary}\n")

    

obj = Emp("Shaam",27,8000)
obj.display_details()
obj.display_instance_details()



