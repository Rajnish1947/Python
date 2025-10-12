def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Take input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD of", x, "and", y, "is", gcd(x, y))
