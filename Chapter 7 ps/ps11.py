#Write a program to print the multiplication table of n using loops in reversed order                                                                  
#======================================================

n = int(input("Enter the number to print  the multiplication table: "))

for i in range(10 , 0, -1):
    print(f"{n} x {i} = {n*i}")
    
