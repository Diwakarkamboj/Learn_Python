s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s)) #length is 2  
#because 20 and 20.0 are different objects in memory even though they have the same value

se = {}
print(type(se))
