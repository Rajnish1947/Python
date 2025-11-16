# Move All Zeros to the End



nums = [0, 1, 0, 3, 12]
pos = 0

for i in range(len(nums)):
    if nums[i] != 0:
        temp = nums[pos]     
        nums[pos] = nums[i]  
        nums[i] = temp        
        pos += 1

print(nums)
