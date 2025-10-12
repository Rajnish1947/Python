# Given two strings s and t, return true if
# t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

def annagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    freq={}
    for i in str1:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i in str2:
        if i not in freq:
            return False
        
        freq[i] -= 1 
        if freq[i] < 0:
            return False    


    return True                
str1="listen"
str2="silent"
print(annagram(str1,str2))