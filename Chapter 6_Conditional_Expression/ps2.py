subject1 = int(input("Enter the subject1 marks"))
subject2 = int(input("Enter the subject2 marks"))
subject3 = int(input("Enter the subject3 marks"))


total_perc =  (((subject1 + subject2 + subject3)/3)*100)/100
print(total_perc)

if(total_perc >= 40):
    if(subject1 >= 33 and  subject2 >= 33 and subject3 >= 33):
        print("You are pass")
    else:
        print("You are fail in any one subject")
else:
    print("You are fail")


