import math

# Prime numbers are those numbers which are divisible by 1 and itself only.

try:
    Num_input = input("Please enter a number to check if number is prime or not: ")
    Num = int(Num_input)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
    exit(1) 
is_prime = True

if Num <= 1:
    is_prime = False
elif Num == 2:
    is_prime = True  # 2 is the only even prime number
elif Num % 2 == 0:
    is_prime = False  # All other even numbers are not prime
else:
    for i in range(3, int(math.sqrt(Num)) + 1, 2):
        if Num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{Num} is a prime number")
else:
    print(f"{Num} is not a prime number")
