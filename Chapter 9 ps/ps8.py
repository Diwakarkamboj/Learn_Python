# Write a program to make a copy of a text file “this.txt”

with open("this.txt") as f:
    content = f.read()
    with open("this_copy.txt", "w") as f2:
         f2.write(content)
print("copy of a text file \"this.txt\" is done and  saved as \"this_copy.txt\"")
