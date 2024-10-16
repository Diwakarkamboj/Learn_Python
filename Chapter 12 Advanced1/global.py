a = 89

def fun():
   global a #this will make a global variable
   a = 3
   print(a)
    
fun()
print(a)