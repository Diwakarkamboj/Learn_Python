#write a progrm to find if a given number is prime or not
#==============================================

#Prime numbers are those  numbers which are divisible by 1 and itself only.

Num = int(input("Please enter a number to check if number is prime or not: "))

is_prime = True

if Num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, Num):
        if(Num % i == 0):
            is_prime = False 
            break   

if is_prime:
    print(f"{Num} is a prime number")
else:
    print(f"{Num} is not a prime number")



