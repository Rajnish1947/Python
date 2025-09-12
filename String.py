# Declare a string
name = 'pooja'

# Basic print
print("Hi.\nHow are you?")  # \n = new line

# Accessing characters by index (0-based)
print("Character at index 3:", name[3])  # Output: 'j'

# String slicing
print("First 3 letters:", name[0:3])     # 'poo'
print("Last 2 letters:", name[-2:])      # 'ja'

# String length
print("Length of name:", len(name))      # 5

# String methods
print("Uppercase:", name.upper())        # 'POOJA'
print("Lowercase:", name.lower())        # 'pooja'
print("Capitalize:", name.capitalize())  # 'Pooja'
print("Title:", name.title())            # 'Pooja'

# Replace
print("Replace 'o' with '@':", name.replace('o', '@'))  # 'p@@ja'

# Count a character
print("Count of 'o':", name.count('o'))  # 2

# Check if string starts/ends with something
print("Starts with 'po':", name.startswith('po'))  # True
print("Ends with 'ja':", name.endswith('ja'))      # True

# Find position
print("Find index of 'j':", name.find('j'))  # 3

# String concatenation
greeting = "Hello"
print(greeting + ", " + name + "!")  # 'Hello, pooja!'

# Repeat string
print(name * 3)  # 'poojapoojapooja'

# Remove whitespace
text = "  hello  "
print("Trimmed text:", text.strip())

# Check if string is digit, alpha, etc.
print("Is 'pooja' alphabetic?:", name.isalpha())    # True
print("Is '123' numeric?:", "123".isdigit())        # True

# Convert string to list
char_list = list(name)
print("List of characters:", char_list)  # ['p', 'o', 'o', 'j', 'a']

# Join characters
joined = "-".join(char_list)
print("Joined with dashes:", joined)     # 'p-o-o-j-a'
