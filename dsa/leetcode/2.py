num = [2, 7, 11, 15]

def max_subarray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

print("Maximum Subarray Sum:", max_subarray(num))  # Output: 35
