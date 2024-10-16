try:
    a = int(input("Ente a number: "))
    print(a)

except Exception as e:
    print(e)
    
else:
    print("I'm inside else block")