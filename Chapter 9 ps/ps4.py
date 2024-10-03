#A file contains a word “Donkey” multiple times. You need to write a
#  program which replace this word with ##### by updating the same file.

repl_Word = "#####"

with open("donkey.txt") as f:
    file_txt = f.read()
    with open("donkey.txt", "w") as h:
        h.write(file_txt.replace("Donkey", repl_Word))

print("Replaced word in file")

    
    