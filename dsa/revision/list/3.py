# Remove Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))   # convert to set (remove duplicates), then back to list
print(unique_nums)

# anotherway
lists = [1, 1, 2, 4, 5, 6, 6, 3]

unique_list = []
for i in lists:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)





