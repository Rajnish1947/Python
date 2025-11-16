# Find the Maximum and Minimum Element in a List

list =[2,4,5,7,9,1]
max=list[0]
min=list[0]

for n in list:
    if n>max:
        max=n
    if n<min:
        min=n
print("max value is",max)
print("min values is",min)        
