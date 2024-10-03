#Repeat program 4 for a list of such words to be censored.

list = ["Cat", "Donkey", "Mouse", "Bird", "Fish"]
repl_word = "$$$$$"
list_len = len(list)

with open("censorList.txt") as f:
    stmt = f.read()
    for i in range(0, list_len):
      stmt = stmt.replace(list[i],repl_word)

with  open("censorList.txt", "w") as f2:
     f2.write(stmt)
            
print("Replaced Successfully")
            
        
        
