nums = [0,1,0,3,12]
i=0
j=1

while j < len(nums):
    if nums[i] == 0 and nums[j] != 0:
        nums[i],nums[j]=nums[j] ,nums[i]
        i+=1
        j+=1
    elif  nums[i]==0 and nums[j] == 0:
          j+=1
    else:
        i+=1
        j+=1      

print(nums)         
    
