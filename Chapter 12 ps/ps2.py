#Write a program to print third, fifth and seventh element from a list using enumerate function.

myList = [1,2,3,4,12,33,44,11]

for index, item in enumerate(myList):
    if index == 2 or index == 4 or index == 6:
        print(f"The {index+1}th element is {item}")
