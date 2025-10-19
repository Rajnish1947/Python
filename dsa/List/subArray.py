def SubArray():
    lists = [1, 2, 3, 4, 5, 6, 7]
    n = len(lists)

    for i in range(n):
        subarray = []                 # empty list for new subarray
        for j in range(i, n):   
            subarray.append(lists[j])  # manually add element
            print(subarray)               # print current subarray

SubArray()

# u can also use this
lists = [1, 2, 3, 4, 5, 6, 7]
n = len(lists)

for i in range(n):            # outer loop
    for j in range(i, n):     # inner loop
        print( lists[i:j+1])
