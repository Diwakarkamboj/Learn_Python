#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poems.txt") as f:
   data = f.read()
   a = data.find("Twinkle")
   if(a>0):
    print(True)
   else:
        print(False)


# with open ("poems.txt") as f:
#     data = f.read()
#     if "Twinkle" in data:
#         print("Twinkle is in the poem")
#     else:
#         print("Twinkle is not in the poem")