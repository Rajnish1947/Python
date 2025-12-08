num = 153
sum_digits = 0
temp = num
n = len(str(num))  # Number of digits

while temp > 0:
    digit = temp % 10       # Last digit
    sum_digits += digit ** n
    temp //= 10             # Remove last digit

if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
