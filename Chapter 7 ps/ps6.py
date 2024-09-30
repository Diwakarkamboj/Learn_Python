#write a progrm to find the sum of first n natural numbers using while loop
#==============================================

num = int(input("Enter  the number to process: ")) 

sum = 0
i = 1

while i<=num:
    sum = sum + i
    i += 1

print(f"Sum of first n natural numbers is {sum}")