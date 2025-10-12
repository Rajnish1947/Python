# Given an integer array nums, find the contiguous subarray (containing at least one number)
#  which has the largest sum and return its sum.

# Example

# Input:

# nums = [-2,1,-3,4,-1,2,1,-5,4]


# Output:

# 6
def maxSubArray(arr):
    current_sum=0
    maxsub=0

    for i in range(len(arr)):
      current_sum+=arr[i]
      if current_sum>maxsub:
         maxsub=current_sum
      if current_sum<0:
         current_sum=0   
    return maxsub
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))    
