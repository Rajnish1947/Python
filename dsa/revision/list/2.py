# Reverse a List Without Using reverse()

list=[1,2,3,5,6,7]

reversedlist=[]

for i in list:
    reversedlist=[i]+reversedlist
print(reversedlist)    


# Example:
# nums = [1, 2, 3]
# reversed_list = []


# Ab loop chalega 

#  Step 1:

# i = 1
# reversed_list = []

# ➡ [i] ka matlab [1] (ek element wali list).
# ➡ [i] + reversed_list = [1] + []

#  Jab hum do lists ko + karte hain, Python dono ko jod deta hai.

# [1] + [] = [1]


# So:

# reversed_list = [1]

# Step 2:

# i = 2
# reversed_list = [1]

# Ab:

# [i] + reversed_list = [2] + [1] = [2, 1]


# So:

# reversed_list = [2, 1]

# Step 3:

# i = 3
# reversed_list = [2, 1]

# Ab:

# [i] + reversed_list = [3] + [2, 1] = [3, 2, 1]

# reversed_list = [3, 2, 1]
#  Output:
# [3, 2, 1]