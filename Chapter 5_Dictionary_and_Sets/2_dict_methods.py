marks = {
    "dwkr" : 100,
    "kk" : 44,
    "Joma" : 88,
    0  : "kim"

}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"dwkr": 98, "John" : 100})
print(marks.items())

print(marks.get("dwkr"))
print(marks["dwkr"])

print(marks.get("dwkr2")) #return none  if key is not found and program will not terminate

print(marks["dwkr2"])# return error

# get(): More flexible, won't break your program if the key doesn't exist.
# [] (Square brackets): Stricter, will raise an error if the key is not found, 
# which can be useful if you want to catch or prevent missing keys.