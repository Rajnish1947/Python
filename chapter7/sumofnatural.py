n=int(input("Enter your first natural number: "))

sum=0

if n<=0:
    print("Enter a valid number")
else:
    for i in range(1,n+1):
        sum+=i
    print("The sum of first",n,"natural numbers is:",sum)