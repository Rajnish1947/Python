# unique number
numset = set()   # empty set

for i in range(1, 8):
    num = int(input("Enter a number: "))
    numset.add(num)   # add() use karna hai

print("Unique numbers:", numset)
