#Write a python function to print multiplication table of a given number.

# def mul(n):
#     for i in range(1, 11):
#         m = n * i
#         print(f"{n} * {i} = {m}") 

# m = mul(3)


def mul(m, i):
    if(m<1):
        print("Invalid Number")
    else:
        print(m *  mul(i))
        i+=1
     
m = mul(3,1)
