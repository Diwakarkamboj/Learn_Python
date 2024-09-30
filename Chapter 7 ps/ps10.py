#Write a program to print the following star pattern
#  *  *  *                                            
#  *     *                                     
#  *  *  *                                                                      
#======================================================

n = 3

for i in range(1, n+1):
    for j in range(1, n+1):
        if(i ==2 and j==2):
            print(" D ", end = "")
        else:
            print(" * ", end = "")
    print()
    


