#Write a program to mine a log file and find out whether it contains ‘python’.

word_present = True

with open("logfile.txt") as f:
    file_txt = f.read()
    if "python" in file_txt:
        word_present = True
    else:
        word_present = False
        

if(word_present):
    print("The word 'Python' is present in the log file.")
else:
    print("Python not found in the log file")
        