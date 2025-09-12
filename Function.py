def functionfirst():
    print("it is my first function")
        
functionfirst()
# . Function with Parameters
def greet(name):
    print("Hello", name)

greet("Ravi")
# Function with Return Value
def square(x):
    return x * x

result = square(4)
print("Square:", result)

# Default Parameters
def info(name="Guest"):
    print("Welcome", name)

info()
info("Raj")

# add the value
def add(num1,num2):
    return num1+num2
print(add(3,4))
