# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

#the statement can be written using with statement

with open("file.txt")  as f:
    data = f.read()
    print(data)

