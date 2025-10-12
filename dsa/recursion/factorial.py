def factor(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factor(n-1)

print(factor(5))

# # BY LOOP
# def byloop():
#     print("BY LOOP PRINT ")
#     num = int(input("Enter the number:")) 
#     if num == 0 or num == 1:
#         print(1)
#         return
#     fact = 1
#     for i in range(2, num + 1):
#         fact = fact * i
#     print(fact)

# byloop()

