def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter the number:"))

for i in range(num):
    print(fibonacci(i),end=" ")
