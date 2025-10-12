def twoSum(arr,target):
    
    n=len(arr)
    dict1={}
    for i in range(n):
        reminder=target-arr[i]
        if reminder in dict1:
            return (dict1[reminder],i)

        dict1[arr[i]]=i
target=9
arr=[2,7,11,15]
print(twoSum(arr,target))

