#Write a program to print the following star pattern
#  *                                             
#  *  *                                      
#  *  *  *                                   
#  *  *  *  *                                  
#======================================================

num = int(input("Enter num to genrate * triangle: "))

for i in range (1, num + 1):
    print(' ' * num)
    print('*' * (i), end = '')


#2nd Approach

# n = 5
# for i in range (1, n+1):
#     print("*" * i)

#======================================================
#3rd approach for opposite  triangle
# n = 5
# for i in range (1, n+1):
#     print("*" * (n-i))
    

    

       

        


