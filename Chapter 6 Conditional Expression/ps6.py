marks = int(input("ENTER THE MARKS"))

if(marks >90 and marks<=100):
    print("Grade Ex")
elif(marks >80 and marks<=90):
    print("Grade A")
elif(marks >70 and marks<=80):
    print("Grade B")
elif(marks >60 and marks<=70):
    print("Grade C")
elif(marks >50 and marks<=60):
    print("Grade D")
elif(marks <=50):
    print("Grade F")
else:
    print("Invalid Marks")