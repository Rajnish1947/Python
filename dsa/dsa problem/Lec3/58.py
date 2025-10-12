# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    return len(words[-1])

# Test
print(lengthOfLastWord("Hello World"))       # 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(lengthOfLastWord("luffy is still joyboy"))        # 6
