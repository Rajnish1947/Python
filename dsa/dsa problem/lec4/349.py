# Problem: Intersection of Two Arrays (LC 349)
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique.
# You may return the result in any order.
# Example 1:
# Input:
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# Output:
# [2]

def intersection(arr1,arr2):
    set1=set(arr1)
    set2=set(arr2)

    return list(set1& set2)

    
arr1=[1,2,4,5,6,7]
arr2=[1,6,7,5]            
print(intersection(arr1,arr2))
    