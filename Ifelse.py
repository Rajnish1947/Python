# -----------------------------
# 1. SIMPLE IF
# -----------------------------
num = int(input("Enter a number (check if > 5): "))
if num > 5:
    print("The number is greater than 5")

# -----------------------------
#  IF-ELSE
# -----------------------------
age = int(input("\nEnter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# -----------------------------
#  3. IF-ELIF-ELSE
# -----------------------------
marks = int(input("\nEnter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# -----------------------------
#  4. NESTED IF
# -----------------------------
number = int(input("\nEnter a number (check range): "))
if number >= 0:
    if number <= 100:
        print("Number is between 0 and 100")
    else:
        print("Number is greater than 100")
else:
    print("Number is negative")

# -----------------------------
#  5. IF WITH LOGICAL OPERATORS
# -----------------------------
x = int(input("\nEnter a value for x: "))
if x > 10 and x < 20:
    print("x is between 10 and 20")

if x < 5 or x > 15:
    print("x is less than 5 or greater than 15")

# -----------------------------
#  6. SHORT HAND IF-ELSE (TERNARY)
# -----------------------------
a = int(input("\nEnter value of a: "))
b = int(input("Enter value of b: "))
max_val = a if a > b else b
print("Maximum is:", max_val)

# -----------------------------
# 7. IF WITH LOOP AND LIST
# -----------------------------
print("\nEnter 5 numbers to check even/odd:")
numbers = []
for i in range(5):
    val = int(input(f"Enter number {i+1}: "))
    numbers.append(val)

for n in numbers:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
