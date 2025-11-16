# The join() function is used to combine (join) a list of strings 
# into a single string, with a chosen separator.
words = ['I', 'love', 'Python']
# list ko strig me convert karne ke liye 
sentence = " ".join(words)
print(sentence)      # Output: I love Python

fruits = ['apple', 'banana', 'grape']
joined = ",".join(fruits)
print(joined)        # Output: apple,banana,grape

text = "Hello world from Python"
#string into list 
words = text.split()
print(words)    # Output: ['Hello', 'world', 'from', 'Python']
# Join with hyphen
result = "-".join(words)

print(result)        # Output: Hello-world-from-Python




