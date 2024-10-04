class Employee:
    inc = 20

    @property
    def salaryAfterIncrement(self):
        return f"{self.salary, ((self.salary * self.inc))/100} totalNewSalary: {((((self.salary * self.inc))/100) + self.salary)}"


    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.salary = salary

prevSalary = 10000

a  = Employee()
a.salaryAfterIncrement = prevSalary
print(a.salaryAfterIncrement)


