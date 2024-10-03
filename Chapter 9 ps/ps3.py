#Write a program to generate multiplication tables from 2 to 20 
# and write it to the different files. Place these files in a folder for a 13 – year old.

folder_path = "E:/python/Chapter 9 ps/Tables/"

for  i in range(2, 31):
        file_name = f"{folder_path}Table_{i}.txt"
        with open(file_name, "w") as  f:
            f.write('\n')
            for j in range(1, 11):
                num = i * j
            f.write(str(i) + " * " + str(j) + " = " + str(num) + '\n')
            
print("Multipication table files are generated.")