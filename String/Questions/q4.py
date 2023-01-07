# Given a string, if the first or last chars are 'x', 
# print the string without those 'x' chars, and
#  otherwise return the string unchanged.

# "xHix" → "Hi"
# "xHi" → "Hi"
# "Hxix" → "Hxi"
# "xxHixx" → xHix

# if I find first and last char 
# then apply replace method for changin x to nothing
print("Enter string")
var = input()
first_ch = var[0]
last_ch = var[len(var)-1]
first_ch = first_ch.replace("x","")
last_ch = last_ch.replace("x","")

# i need to get part of the string where 
# first and last letters are not included.

var = var[1:len(var)-1]
var = first_ch + var + last_ch
print(var)

# Do I need this original variable again? 
# If yes, don't reassign the variable
# to keep original value. 
# if no, it is up to you to reassign it or not. 
# len -> length