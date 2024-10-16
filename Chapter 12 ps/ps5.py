#Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Please enter a number to generate a table: "))

mulList = [num*i for i in range(1,11)]

f1 = open('1.txt', 'w')
f1.write(str(mulList))

print("File is created and multiplication table is added in it")
f1.close()
        
    
   