T1 = (1,'BB','Cool',44,555,6666,555,'Cool','BB',44)
T2 = (1, 5, 3, 99, 2, 0)

count_NUM = T1.count(44)
print(count_NUM)

index = T1.index('Cool')
print(index)

# to check tuple length
print(len(T1)-1)
print(max(T2))
print(min(T2))
print(sum(T2))

# in and not in to check if value is present in tuple or not
print(99 in T2)
print('Cool' in  T1)
print('Cool' not in  T1)

#Tupel is immutable like string

# we can add 2 tuples
T3 = T1 + T2
print(T3)

# tuple repetition
print(T1*2)

#slicing and indexing in tuple
print(T1[3:5])

#unpacking
a, b, c,  d, e, f, g, h, i, j = T1

print(a)
