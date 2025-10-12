def are_anagrams(s1, s2):
    if s1!=s2:
        return 
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
