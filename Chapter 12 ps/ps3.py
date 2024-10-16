#Write a list comprehension to print a list which contains the multiplication table
# of a user entered number.

###########################################################################

num = int(input("Please enter a number to generate a table: "))

mulList = [num*i for i in range(1,11)]

print(mulList)





