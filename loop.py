# ALL PYTHON LOOP EXAMPLES IN ONE FILE

# ----------------------------------------

i=1
while i<6 :
    print(i)
    i=i+1
    
for latters in 'rajnish':
    print(latters)    

list=["rani",'kajal','suman','soniya']

for values in list:
    print(values)


# # 1. For Loop with range()
# print("1. For Loop with range:")
# for i in range(5):  # 0 to 4
#     print("i =", i)

# # ----------------------------------------
# # 2. While Loop
# print("\n2. While Loop:")
# i = 1
# while i <= 5:
#     print("i =", i)
#     i += 1

# # ----------------------------------------
# # 3. For Loop over List
# print("\n3. For Loop over List:")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # ----------------------------------------
# # 4. For Loop over String
# print("\n4. For Loop over String:")
# for ch in "python":
#     print(ch)

# # ----------------------------------------
# # 5. For Loop over Tuple
# print("\n5. For Loop over Tuple:")
# nums = (1, 2, 3)
# for n in nums:
#     print(n)

# # ----------------------------------------
# # 6. For Loop over Dictionary
# print("\n6. For Loop over Dictionary:")
# person = {"name": "Raj", "age": 21}
# for key, value in person.items():
#     print(key, "=>", value)

# # ----------------------------------------
# # 7. Loop with break
# print("\n7. Break in Loop:")
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# # ----------------------------------------
# # 8. Loop with continue
# print("\n8. Continue in Loop:")
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# # ----------------------------------------
# # 9. Loop with pass
# print("\n9. Pass in Loop:")
# for i in range(3):
#     pass  # does nothing
# print("Pass used successfully.")

# # ----------------------------------------
# # 10. Nested Loops
# print("\n10. Nested Loop:")
# for i in range(2):
#     for j in range(3):
#         print(f"i={i}, j={j}")

# # ----------------------------------------
# # 11. Infinite Loop (with break)
# print("\n11. Infinite Loop with Break:")
# count = 0
# while True:
#     print("Running...")
#     count += 1
#     if count == 3:
#         break

# # ----------------------------------------
# # 12. For Loop with enumerate()
# print("\n12. Loop using enumerate:")
# colors = ['red', 'green', 'blue']
# for index, color in enumerate(colors):
#     print(index, color)

# # ----------------------------------------
# # 13. Loop through sorted list
# print("\n13. Sorted Loop:")
# nums = [4, 1, 3, 2]
# for num in sorted(nums):
#     print(num)

# # ----------------------------------------
# # 14. Reverse Loop
# print("\n14. Reverse Loop:")
# for i in reversed(range(5)):
#     print(i)
