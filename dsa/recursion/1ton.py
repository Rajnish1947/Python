# Recursion Method
n = int(input("Enter your number: "))

def printnum(i, n):
    if i > n:
        return
    print(i)
    printnum(i + 1, n)

printnum(1, n)

# Using For Loop
print("By for loop")
n = int(input("Enter your number: "))
for i in range(1, n + 1):
    print(i)

# Using While Loop
print("By while loop")
i = 1
while i <= n:
    print(i)
    i += 1



