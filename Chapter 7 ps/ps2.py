#Write a program to greet all the person name stored in a list 'l' and which starts with S
#==============================================

l = ['Harry', 'Sohan', 'Sachin', 'Rahul', 'Dinesh']
    
#1st Approach

for i  in range (0, len(l)):
    if("S" in l[i]):
        print(f'Hello {l[i]}')

for i  in range (0, len(l)):
    if("S" not in l[i]):
        print(f'GM {l[i]}')

#2nd Approach

for k in l:
    if k.startswith("S"):
        print(f"Hello {k}")

for k in l:
    if not k.startswith("S"):
        print(f"Hello {k}")       
        
    

        