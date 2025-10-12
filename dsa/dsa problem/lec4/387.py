# Given a string s, find the first non-repeating character in 
# it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
def firstChar(s):
    n = len(s)
    st = {}           # dictionary for frequency
    ans = -1          # default answer

    # Step 1: Count frequency of each character
    for i in range(n):
        if s[i] not in st:
            st[s[i]] = 1
        else:
            st[s[i]] += 1

    # Step 2: Find first index jiska freq = 1
    for i in range(n):
        if st[s[i]] == 1:
            ans = i
            break
    
    return ans
str1="leetcode"
str2="loveleetcode"
str3="aabb"

print(firstChar(str1))      # 0
print(firstChar(str2))  # 2
print(firstChar(str3))   
      