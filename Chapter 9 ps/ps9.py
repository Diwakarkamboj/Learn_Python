#Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    content = f.read()
    with open("this_copy.txt") as f2:
         content2 = f2.read()
    if(content in content2):
        print("Yes contents are matched")
    else:
        print("No, contents not matched")