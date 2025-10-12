s = "hello"

# Change first character
s2 = "H" + s[1:]  # "Hello"

# Append
s3 = s + "!"      # "hello!"

# Remove / replace
s4 = s.replace("l", "x")  # "hexxo"

# Sort
s5 = "".join(sorted(s))    # "ehllo"

# Reverse
s6 = s[::-1]               # "olleh"
