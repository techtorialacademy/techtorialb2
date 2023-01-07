#    012345
a = "Python"

# Accesing the element
# We are using index number of a character to acces elemnt

print(a[2]) # t

# I need to learn position of the letter h?
# To learn index number of a given character
# we use find method. 
print(a.find("h")) # 3
# Return type of find method is integer. 

print(type(a.find("h")))


var2 = "Encapsulation is good for data hiding"

print(var2.find("a")) # 3
# Even character is repeating through out the 
# string it will return first index number of given 
#character

#rfind() method
#This method will help us to get 
# last position of a given character.
print(var2.rfind("a")) #29

var3 = "Python Python"

print(var3.find("hon")) #3

# 3
# Even multiple characters are passed 
# as an argument to find method
# it will return the index number of first 
# character.

print(var3.find("Peter")) # 

# When the argument given in the find method
# doesn't exist in the string, find method 
# will return -1

print(var3.find("z")) # -1

print(var3.rfind("th")) # 9

# Find index of all the m's in this string
var4 = "Programmmming"








