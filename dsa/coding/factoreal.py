def factoreal(n):
    if n==0:
        return 1
    return n*factoreal(n-1)  
print(factoreal(5))