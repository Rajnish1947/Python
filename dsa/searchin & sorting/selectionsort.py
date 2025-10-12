# Selection Sort ek comparison-based in-place sorting algorithm hai jo array me repeatedly minimum (ya maximum) element select karke usko sahi position par place karta hai.
# Array ko do parts me divide karta hai:
# Sorted part (shuru me empty)
# Unsorted part (poora array initially)

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Test
arr = [64, 25, 12, 22]
print(selection_sort(arr))  # Output: [12, 22, 25, 64]
