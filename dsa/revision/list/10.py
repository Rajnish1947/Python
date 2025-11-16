# Find All Pairs Whose Sum Equals Target

nums = [1, 5, 7, -1, 5]
target = 6

# Step 1: Sort the list first
nums.sort()  # [-1, 1, 5, 5, 7]

# Step 2: Initialize pointers
left = 0
right = len(nums) - 1

while left < right:
    sum=nums[left]+nums[right]
    if sum==target:
        print(nums[left] ,nums[right])
        left += 1
        right -= 1
    elif sum<target:
        right+=1
    else:
        right-=1        