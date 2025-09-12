num = int(input("Enter your number: "))

# Method 1: Using for loop
print("\nUsing for loop:")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Method 2: Using while loop
print("\nUsing while loop:")
i = 1   # reset i back to 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

