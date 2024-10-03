#Write a program to find out the line number where python is present from ques 6.
l = []
nf = []
with open("logfile.txt") as f:
    file_lst = f.readlines()
    for i in range(len(file_lst)):
        if "python" in file_lst[i].lower():
            l.append(i+1)
            #print(f"Python word is found in the file on line number {i}")
        else:
            nf.append(i+1)
            #print(f"Python word is not found in the file on line number {i}")

print(f"List of line numbers where python word is found is {l}")  
print(f"List of line numbers where python word is not found is {nf}")         
  
        
