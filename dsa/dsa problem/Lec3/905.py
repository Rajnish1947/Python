# Problem Statement

# Given an integer array nums, move all even integers to the beginning of 
# the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Example

# Input:

# nums = [3,1,2,4]


# Output:

# [2,4,3,1]


def sortEvenbeginning(arr):
    start = 0
    if len(arr) == 0:   
        return arr
    else:
        for i in range(len(arr)):
         if arr[i]%2==0:
                temp=arr[i]
                arr[i]=arr[start]
                arr[start]=temp
                start+=1
    return arr


arr = [1, 2, 3, 5, 7, 3, 4, 8, 9, 6]
print(sortEvenbeginning(arr))
