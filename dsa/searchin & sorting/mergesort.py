# Merge Sort Definition
# Merge Sort ek Divide and Conquer algorithm hai.
# Ye array ko repeatedly do equal parts me divide karta hai, har part ko recursively sort karta hai,
# aur phir dono sorted parts ko merge karke final sorted array banata hai.
# Ye stable sorting algorithm hai (same elements ka relative order maintain hota hai).


def merge_sort(arr):
    if len(arr) <= 1:
        return arr   # base case

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # left half
    right = merge_sort(arr[mid:])  # right half

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # merge both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  #  [3, 9, 10, 27, 38, 43, 82]



