# Insertion Sort ek simple comparison-based sorting algorithm hai jo array ko ek-ek karke sorted part banाता है.
# Ye algorithm array ko do parts me divide karta hai:
# Sorted part (shuru me sirf pehla element hota hai)
# Unsorted part (baaki ke elements)
# Har step me ek element unsorted part se uthakar usko sorted part me sahi jagah insert kar dete hain.
# Ye exactly waise hi kaam karta hai jaise tum apne haath me cards ko arrange karte ho – ek ek card ko sahi position me dalte ho.

# Best Case (already sorted): O(n)
# Worst Case (reverse sorted): O(n²)
# Space Complexity: O(1) (in-place algorithm)

def inserSort(arr):
    n = len(arr)
    for i in range(1, n):            # Step 1: pick element from index 1 to n-1
        key = arr[i]                  # Step 2: key = current element to insert
        j = i - 1                     # Step 3: start comparing with previous element

        while j >= 0 and arr[j] > key:  # Step 4: shift elements greater than key to the right
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key                # Step 5: place key in correct position

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(inserSort(arr))
