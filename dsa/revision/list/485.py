def maxcon(nums):

    count =0
    maxcunt=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1
        else:
            maxcunt=max(maxcunt,count)
            count=0   
    return  max(maxcunt,count)        
nums = [1,1,0,1,1,1,0,1,1,1,1]
print(maxcon(nums))
