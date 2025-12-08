def linear_search(arr, target):
    # Loop through array
    for i in range(len(arr)):
        if arr[i] == target:   # Check each element
            return i           # Found → return index
    
    return -1  

arr = [12, 5, 9, 34, 8, 15]
print(linear_search(arr, 34))
