num=[2,7,11,15]
target=9

def sum(num,target):
    l=0
    r=len(num)-1
    while l<r:

        s = num[l] + num[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []     

  
print(sum(num,target) )