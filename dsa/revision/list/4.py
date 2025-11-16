# Count Frequency of Each Element in a List
# “Count frequency of each element in a list” ka matlab hota hai —
#  ek list me har unique element kitni baar repeat hua hai, wo count karna.
# Example:
# lis = [1, 1, 2, 4, 5, 6, 6, 3]
# Yahan elements hai:
# 1 → 2 baar aaya
# 2 → 1 baar
# 4 → 1 baar
# 5 → 1 baar
# 6 → 2 baar
# 3 → 1 baar

# agar keval element check karana ho to

lis = [1, 1, 2, 4, 5, 6, 6, 3]
count=0
for i in lis:
    count+=1
print(count)    

# count frequenty of element

lost =[1, 1, 2, 4, 5, 6, 6, 3]

freq ={}

for i in lost:
    if i in freq:
        freq[i]+=1
    else:
         freq[i]=1    


print(freq)         
