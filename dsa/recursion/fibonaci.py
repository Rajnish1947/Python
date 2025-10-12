# Recursive function to get nth Fibonacci number
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(n, i=0):
    if i < n:
        print(fibonacci(i), end=" ")
        print_fibonacci(n, i+1)

# Take input from user
n = int(input("Enter the number of Fibonacci numbers to print: "))
print_fibonacci(n)


# # Take input from user
# n = int(input("Enter the number of terms: "))

# # Using Recursion
# print("Fibonacci series (Recursion):")
# for i in range(n):
#     print(fibonacci(i), end=" ")
# print()  # newline

# # Using Iteration / Loop
# print("Fibonacci series (Loop):")
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

        