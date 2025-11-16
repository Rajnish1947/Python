# Count frequency of characters in a string using dictionary

s="babanana"

freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1

print(freq)    
