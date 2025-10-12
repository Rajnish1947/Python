# Problem Statement (LeetCode 151)

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters.

# Remove extra spaces (leading, trailing, and multiple spaces).

# Example:

# Input: "  the sky   is  blue "
# Output: "blue is sky the"
# LeetCode 151: Reverse Words in a String

# ----------------------------
# Method 1: Pythonic way
# ----------------------------
def reverseWords_pythonic(s: str) -> str:
    # split removes extra spaces, join reconstructs
    words = s.split()
    return " ".join(words[::-1])

# ----------------------------
# Method 2: Manual Two-Pointer (Interview Style)
# ----------------------------
def reverseWords_manual(s: str) -> str:
    s = s.strip()   # remove leading/trailing spaces
    words = []
    i = 0
    while i < len(s):
        if s[i] == " ":
            i += 1
            continue
        j = i
        while j < len(s) and s[j] != " ":
            j += 1
        words.append(s[i:j])  # collect a word
        i = j
    words.reverse()  # reverse the list of words
    return " ".join(words)


# ----------------------------
# Test Cases
# ----------------------------
test_strings = [
    "  the sky   is  blue ",
    " hello world ",
    "a good   example"
]

for ts in test_strings:
    print(f"Input: '{ts}'")
    print("Pythonic way  →", reverseWords_pythonic(ts))
    print("Manual way    →", reverseWords_manual(ts))
    print("-" * 40)
