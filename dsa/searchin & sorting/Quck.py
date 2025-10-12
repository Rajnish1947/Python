# Quick Sort Algorithm
# QuickSort is a Divide and Conquer algorithm.
# Steps:
# Pick a pivot element.
# Partition the array so that elements smaller than pivot go left, and bigger go right.
# Recursively apply quicksort on left and right subarrays.

def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1         # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:   # if current element <= pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]   # swap

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Sort left and right parts
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver Code
arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)

quickSort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)
