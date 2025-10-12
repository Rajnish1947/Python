# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# built function
# def replace(str):
#     res=str.replace('.','[.]')
#     return res
# str= "1.1.1.1"
# print(replace(str))  

# another way

def replace(str):
    newstr=""
    for i in str :
        if i !=".":
            newstr+=i
        else:
            newstr+="[.]"   
    return newstr
str= "1.1.1.1"
print(replace(str))  
         

