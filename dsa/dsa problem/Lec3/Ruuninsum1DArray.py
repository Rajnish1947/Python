# Given an integer array nums, return an array runningSum such that runningSum[i] is the sum of
#  all elements from nums[0] to nums[i] (inclusive).

# Example:

# Input: nums = [1, 2, 3, 4]

# Output: [1, 3, 6, 10]

# Explanation:

# runningSum[0] = 1

# runningSum[1] = 1 + 2 = 3

# runningSum[2] = 1 + 2 + 3 = 6

# runningSum[3] = 1 + 2 + 3 + 4 = 10

nums = [1, 2, 3, 4, 5, 6]

ans = []
ans.append(nums[0])   # first element same as nums[0]

for i in range(1, len(nums)):   # start from index 1
    x = ans[i-1] + nums[i]      # previous sum + current number
    ans.append(x)

print(ans)
