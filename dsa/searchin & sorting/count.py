# Counting Sort?
# Non-comparison sorting algorithm
# Works when the range of numbers (max - min) is not too large.
# It counts occurrences of each element and uses that to place elements in sorted order.

def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    arr.clear()
    for i in range(len(count)):
        arr.extend([i] * count[i])

    return arr


# Driver
arr = [4, 2, 2, 8, 3, 3, 1]
print("Sorted Array:", countingSort(arr))
