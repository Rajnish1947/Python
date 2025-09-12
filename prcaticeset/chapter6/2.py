a = int(input("Enter your number: "))

if a <= 100 and a >= 80:
    print("Your grade is A")
elif a < 80 and a >= 70:
    print("Your grade is B")
elif a < 70 and a >= 50:
    print("Your grade is C")
else:
    print("You are fail")
