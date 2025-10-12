# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
# all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


def isAlphanumeric(ch):
    x = ord(ch)
    # Check if character is a letter or digit
    if 97 <= x <= 122 or 65 <= x <= 90 or 48 <= x <= 57:
        return True
    return False

def validPalindrome(s):
    s = s.lower()
    i, j = 0, len(s) - 1

    while i < j:
        # skip non-alphanumeric from left
        if not isAlphanumeric(s[i]):
            i += 1
            continue

        # skip non-alphanumeric from right
        if not isAlphanumeric(s[j]):
            j -= 1
            continue

        # compare characters
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


# ✅ Example Test
print(validPalindrome("A man, a plan, a canal: Panama"))  # True
print(validPalindrome("race a car"))  # False
