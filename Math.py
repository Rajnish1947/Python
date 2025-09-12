# Basic Numbers
a = 15
b = 4

# Arithmetic Operations
print("Addition:", a + b)             # 19
print("Subtraction:", a - b)          # 11
print("Multiplication:", a * b)       # 60
print("Division:", a / b)             # 3.75
print("Floor Division:", a // b)      # 3
print("Modulus (Remainder):", a % b)  # 3
print("Exponent (Power):", a ** b)    # 15^4 = 50625

# Using built-in round function
print("Rounded division:", round(a / b, 2))  # 3.75

# ----------------------------
# Importing math module
import math

x = 9
y = 2.5

print("\n-- Using math module --")
print("Square root of 9:", math.sqrt(x))        # 3.0
print("Power:", math.pow(a, b))                 # 15.0^4.0
print("Ceil of 2.5:", math.ceil(y))             # 3
print("Floor of 2.5:", math.floor(y))           # 2
print("Absolute of -10:", abs(-10))             # 10
print("Factorial of 5:", math.factorial(5))     # 120
print("Log base e of 10:", math.log(10))        # ~2.302
print("Log base 10 of 100:", math.log10(100))   # 2.0
print("Sin(90° in rad):", math.sin(math.radians(90)))  # 1.0

# Constants
print("\n-- Constants --")
print("PI:", math.pi)
print("Euler's number (e):", math.e)
