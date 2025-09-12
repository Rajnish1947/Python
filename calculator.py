print("----- Simple Calculator -----")

# Taking input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %, **, //): ")
num2 = float(input("Enter second number: "))

# Performing operations
if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
elif operator == '%':
    print("Result:", num1 % num2)
elif operator == '**':
    print("Result:", num1 ** num2)
elif operator == '//':
    print("Result:", num1 // num2)
else:
    print("Invalid operator")

print("----- End of Program -----")
