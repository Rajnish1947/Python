# Find the key with the maximum value

d = {"a": 10, "b": 5, "c": 20}


max_key = None
max_val = float("-inf") 
for i in d:
    if d[i]>max_val:
        max_val=d[i]

print(max_val)        