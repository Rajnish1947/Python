# Quick Sort Algorithm
# QuickSort is a Divide and Conquer algorithm.
# Steps:
# Pick a pivot element.
# Partition the array so that elements smaller than pivot go left, and bigger go right.
# Recursively apply quicksort on left and right subarrays.



def partition(nums, l, r):
    key = nums[r]
    start = l

    for i in range(l, r+1):
        if nums[i] <= key:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start = start + 1   # FIX

    return start - 1            # FIX


def quickSort(nums, l, r):
    if l >= r:
        return

    p = partition(nums, l, r)
    quickSort(nums, l, p - 1)
    quickSort(nums, p + 1, r)


nums = [64, 25, 12, 22, 11, 90]
quickSort(nums, 0, len(nums) - 1)
print(nums)
