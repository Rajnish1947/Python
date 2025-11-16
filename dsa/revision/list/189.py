
nums = [1,2,3,4,5,6,7]
k = 3
def fun(nums,k):
        
  k = k % len(nums)   # to avoid extra rotations
  for i in range(0,k):
          e=nums.pop()
          nums.insert(0,e)
fun(nums, k)
print(nums)