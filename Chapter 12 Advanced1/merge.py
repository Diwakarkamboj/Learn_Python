dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
print(merged)


# the reason why b: 2 is not appearing in the output is that in Python, 
# when merging dictionaries using the | operator (introduced in Python 3.9), 
# if there are duplicate keys between the dictionaries, the value from the dictionary on the
# right side of the | operator will overwrite the value from the dictionary on the left side.
