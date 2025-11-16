# Merge Two Sorted Lists

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

merge=[]

j=i=0
while i < len(a) and j < len(b):
    if a[i]<b[j]:
        merge.append(a[i])
        i += 1

    else:
        merge.append(b[j])
        j += 1

merge+=a[i:]
merge+=b[j:] 
print(merge)           

