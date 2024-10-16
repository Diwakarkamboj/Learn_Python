a = int(input("Enter a number: "))
b = int(input("Enter Second number: "))


if(b == 0):
    raise ZeroDivisionError("a is not divisible by  zero in python")

else:
    print(f"division if numbers are: {a/b}")

print("thanks")