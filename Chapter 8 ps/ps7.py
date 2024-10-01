#Write a python function to remove a given word from a list ad strip it at the same time.


l = ['Apple',"Coole","Hellol","Name"]
print(f"{l} \nWhich word you want to strip ")
word = input("Enter the word you want to strip: ")

def funct(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
    # print(f"List after strip is {word} is {l}")

print(funct(l, word))
