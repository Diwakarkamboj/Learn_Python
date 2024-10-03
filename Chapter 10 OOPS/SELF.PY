class Emp:
    lan = "Python"
    name = "Ram"
    Sal = 120000 #class attributes

    def fun(d):
            print(f"Hello, I am a instance function inside a class that has {d.lan} and {d.name}")

    @staticmethod
    def fun2():
            print(f"Hello, I am a staic function inside a class")

obj = Emp()
obj.name = "Diwakar" 
obj.lan = "Java"

obj.fun() #Emp.fun(obj)
obj.fun2() #Emp.fun2()