class Emp:
    lan = "Python"
    Sal = 120000 #class attributes

cl = Emp()
cl.name = "Diwakar"
print(cl.name, cl.lan, cl.Sal)

cl.name = "Harry"   # Updating the instance/object attribute
print(cl.name, cl.lan, cl.Sal)

cl.lan = "JavaScript"
cl.name = "John"
print(cl.name, cl.lan, cl.Sal)

# instance attribute will be given more preference  than class attribute.
#  If we want to use class attribute then we have to use class name. 
