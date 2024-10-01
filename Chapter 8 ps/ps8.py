#Write a python function to print multiplication table of a given number.

def mul(n):
    for i in range(1, 11):
        m = n * i
        print(f"{n} * {i} = {m}") 

m = mul(3)
