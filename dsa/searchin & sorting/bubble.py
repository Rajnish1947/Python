# Bubble Sort Concept
# Bubble Sort ek simple comparison-based sorting algorithm hai.
# Har pass me adjacent elements ko compare karke unko swap karte hain agar wo galat order me ho.
# Largest element har pass ke baad "bubble" hoke last me chala jata hai.

# Best Case (already sorted): O(n)
# Worst Case (reverse sorted): O(n²)
# Space Complexity: O(1) (in-place algorithm)

def Bublesort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                # for chack if alredy sort ho
                isSwap=False

                # swap
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                isSwap=True
        
        if not isSwap :
            return False  
    return arr            
arr = [64, 34, 25, 12, 22, 11, 90]
print(Bublesort(arr))