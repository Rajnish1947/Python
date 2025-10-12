# 26


# Example 1:
# Input: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
# Output: 1 -> 2 -> 5 (both 3 and 4 values appear more than once, so all occurrences removed) 
# LeetCode
# +1

# Example 2:
# Input: 1 -> 1 -> 1 -> 2 -> 3
# Output: 1 ->2-> 3

def removedublicate(arrs):
    ans = []
    for i in range(len(arrs)-1):
        if arrs[i] != arrs[i+1]:
            ans.append(arrs[i])
    ans.append(arrs[-1])   
    return ans

arr = [1,1,1,2,3]
print(removedublicate(arr))

