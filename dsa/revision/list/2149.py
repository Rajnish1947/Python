nums = [3,1,-2,-5,2,-4]

n=len(nums)
result=[0]*n
postindex=0
negativeindex=1
for i in range (0,n):
    if nums[i]>=0:
        result[postindex]=nums[i]
        postindex+=2
    else:
       result[negativeindex]=nums[i] 
       negativeindex+=2
print(result)       

