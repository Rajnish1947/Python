# 4. Invert a dictionary (swap keys and values)


d = {"a": 1, "b": 2, "c": 3}
inverted = {}

for i in d:
    value=d[i]
    inverted[value]=i
print(inverted)    