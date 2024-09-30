#write a progrm to find the factorial of a given number using for loop
#==============================================

num=int(input("enter num:"))

fact_prod = 1

for i in range (1,num+1):
    fact_prod = fact_prod * i

print(f"{num}! is {fact_prod}")  # Output: factorial of 5 is 120

