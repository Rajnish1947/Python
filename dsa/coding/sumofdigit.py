# Input number
num = 1234
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10       # Last digit
    sum_digits += digit     # Add to sum
    temp //= 10             # Remove last digit

print(f"Sum of digits of {num} is {sum_digits}")
