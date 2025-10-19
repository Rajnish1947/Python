# The join() function is used to combine (join) a list of strings 
# into a single string, with a chosen separator.
words = ['I', 'love', 'Python']
sentence = " ".join(words)
print(sentence)

# I love Python  output

fruits = ['apple', 'banana', 'grape']
joined = ",".join(fruits)
print(joined)

# apple,banana,grape output

text = "Hello world from Python"
# Split into list
words = text.split()
# Join with hyphen
result = "-".join(words)

print(result) # Hello-world-from-Python




