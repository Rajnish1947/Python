def reverseStr(str):
    reverstr=" "
    for char in str:
        reverstr=char+reverstr

    return reverstr    
str1="hello" 
print(reverseStr(str1))       