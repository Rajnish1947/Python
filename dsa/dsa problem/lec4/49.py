
# Function to sort the characters of a string alphabetically
def sortString(s):
    s1 = list(s)      # Convert string to a list of characters
    s1.sort()         # Sort the characters in ascending order
    return "".join(s1)  # Join the sorted characters back into a string

# Function to group anagrams together
def GroupOfAnagrams(strs):
    dict1 = {}  # Dictionary to store groups of anagrams
    for s in strs:
        key = sortString(s)  # Use sorted string as key (all anagrams have same key)
        
        if key in dict1:     # If key already exists in dictionary
            dict1[key].append(s)  # Append current string to the existing list
        else:
            dict1[key] = [s]      # Otherwise, create a new list with current string
    
    return list(dict1.values())  # Return all grouped anagrams as a list of lists

# Example list of strings
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Print the grouped anagrams
print(GroupOfAnagrams(strs))  


       