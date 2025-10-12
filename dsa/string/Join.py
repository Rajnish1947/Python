# ===============================
# Python String join() Method
# ===============================

# 1. Join a list of strings
lst = ["Python", "is", "fun"]
s = " ".join(lst)  # join with space
print("Join with space:", s)  # Output: "Python is fun"

# 2. Join with a different separator
date_parts = ["2025", "09", "28"]
date = "-".join(date_parts)  # join with dash
print("Join with dash:", date)  # Output: "2025-09-28"

# 3. Join a tuple of strings
tpl = ("a", "b", "c")
joined = ",".join(tpl)  # join with comma
print("Join tuple with comma:", joined)  # Output: "a,b,c"

# 4. Join characters of a string
word = "hello"
joined_chars = "-".join(word)  # insert '-' between characters
print("Join characters with dash:", joined_chars)  # Output: "h-e-l-l-o"

# 5. Join numbers (convert to strings first)
nums = [1, 2, 3]
joined_nums = "-".join(map(str, nums))
print("Join numbers with dash:", joined_nums)  # Output: "1-2-3"

# Key Notes:
# - join() is a string method (separator.join(iterable))
# - All elements in iterable must be strings
# - It returns a new string; does not modify original iterable
