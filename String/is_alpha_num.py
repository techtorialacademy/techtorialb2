
var1 = "Techtorial Academy"

print(var1.isalpha())
#    False
# Spaces are not considered as letters, 
# therefore, this will return False. 
print(var1.replace(" ","").isalpha())
# True

var2 = "Weatherisniceoutside."
print(var2.isalpha())
# False


# isnumeric

var3 = "1234567"

print(var3.isnumeric())
# True, all characters are numbers. 

var4 = "1.5"
print(var4.isnumeric())
# False

# isalnum
# It'll return True when string consists of 
# only numbers and letters

var5 = "Phonenumberis23456543"
print(var5.isalnum())
# True

var6 = "#7777777"
print(var6.isalnum())
# False, because # is neither number nor letter

str1 = "first"
str2 = ""
str3 = "anumber7"
str4 = " anumber8"
################
print(str1.isalnum()) # True
print(str1.isalpha()) # True
print(str1.isnumeric())# False
################
print(str2.isalnum()) # False
print(str2.isalpha()) # False
print(str2.isnumeric())# False
################
print(str3.isalnum()) # True
print(str3.isalpha()) # False
print(str3.isnumeric())# False
################
print(str4.isalnum()) # False
print(str4.isalpha()) # False
print(str4.isnumeric())# False






























