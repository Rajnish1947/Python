def countGoodSubstrings(s):
    n = len(s)
    count = 0
    
    for i in range(n - 2):        # window of size 3
        substring = s[i:i+3]      # take substring of length 3
        if len(set(substring)) == 3:  # check all chars distinct
            count += 1
    
    return count

# test case
s = "aababcabc"
print(countGoodSubstrings(s))  # Expected Output = 4









