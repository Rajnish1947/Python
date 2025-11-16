# Check if two dictionaries are equal

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}

equal = True

for k in d1:
    if k  not in d2:
        equal=False
        break
    if d1[k]!=d2[k]:
        equal=False
        break
for k in d2:
    if k not in d1:
        equal=False
        break
print(equal)        
