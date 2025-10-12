# ye only for sorted array

def twoSum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        sum1 = arr[left] + arr[right]
        
        if sum1 == target:
            return [left+1, right+1]   
        elif sum1 < target:
            left += 1   
        else:
            right -= 1   
    
    return []   
        

# Example
target = 9
arr = [1,2,3,4,5,6,7,8,9]
print(twoSum(arr, target))
