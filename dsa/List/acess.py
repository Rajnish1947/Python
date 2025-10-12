fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple (first element)
print(fruits[-1])  # cherry (last element)
print(fruits[1:3]) # ['banana', 'cherry'] (slicing)


fruits[1] = "blueberry"   # change element
fruits.append("orange")   # add item at end
fruits.insert(1, "kiwi")  # insert at position
fruits.remove("apple")    # remove specific element
fruits.pop()              # remove last element
numbers = [10, 20, 30, 40]

print(len(numbers))    # 4
print(sum(numbers))    # 100
print(max(numbers))    # 40
print(min(numbers))    # 10

# access the element 

for fruit in fruits:
    print(fruit)
