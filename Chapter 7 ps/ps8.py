#Write a program to print the following star pattern
#                                               i\j 0 1 2 
#      *                                         0  * * *
#   *  *  *                                      1  * * *
#  *  *  *  *                                    2  * * *

#====================================================== this will work till number 9

num = int(input("Enter num to genrate * triangle: "))

for i in range (1, num+1):
    print(' ' * (num - i), end='')
    print(f"{i} " * i)



