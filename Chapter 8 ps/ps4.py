#Write a recursive function to calculate the sum of first n natural numbers.


def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    # Recursive case: n + sum of numbers from 1 to n-1
    else:
        return n + sum_of_natural_numbers(n - 1) #6+5+4

n = int(input("Enter a number: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is {result}")



        
