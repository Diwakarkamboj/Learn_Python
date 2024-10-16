#Write a program to open three files 1.txt, 2.txt and 3.txt if 
# any these files are not present, a message without exiting the program must be printed prompting the same.

##################################################

def fun():
    try:
        f1 = open('1.txt', 'r')
        f2 = open('2.txt', 'r')
        f3 = open('3.txt', 'r')
    except FileNotFoundError as e:
        print("Files not present ", e)
        
fun()