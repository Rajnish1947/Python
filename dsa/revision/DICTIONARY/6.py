# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Amit", 21, "Delhi"]


d = {}
for i in range(len(keys)):
    d[keys[i]]=values[i]

print(d)    