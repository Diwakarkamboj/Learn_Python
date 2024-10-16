# without using walrus operator

name = input("Enter your name: ")

if(len(name) > 0):
    print(f"Name is: {name}")
else:
    print("Name is empty")  # This will print if the name is empty
    
    
#using walrus operator

if(len(name := input("Enter your name: ")) > 0):
    print(f"Name is: {name}")
else:
    print("Name is empty")