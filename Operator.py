print("\n=== Arithmetic Operators ===")
a = 10
b = 3
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division (float)
print("a // b =", a // b)    # Floor Division
print("a % b =", a % b)      # Modulus
print("a ** b =", a ** b)    # Exponentiation

print("\n=== Assignment Operators ===")
x = 5
print("Initial x =", x)
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x //= 2
print("x //= 2 ->", x)
x %= 3
print("x %= 3 ->", x)
x **= 2
print("x **= 2 ->", x)

print("\n=== Comparison Operators ===")
a = 10
b = 3
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n=== Logical Operators ===")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n=== Bitwise Operators ===")
a = 10    # 1010
b = 3     # 0011
print("a & b =", a & b)     # AND
print("a | b =", a | b)     # OR
print("a ^ b =", a ^ b)     # XOR
print("~a =", ~a)           # NOT
print("a << 1 =", a << 1)   # Left Shift
print("a >> 1 =", a >> 1)   # Right Shift

print("\n=== Membership Operators ===")
my_list = [1, 2, 3, 4]
print("2 in my_list:", 2 in my_list)
print("5 not in my_list:", 5 not in my_list)

print("\n=== Identity Operators ===")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)           # True: same object
print("x is z:", x is z)           # False: same content, different object
print("x is not z:", x is not z)   # True
