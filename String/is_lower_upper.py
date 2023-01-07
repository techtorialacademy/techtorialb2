
s = "Python"

print(s.islower()) # 
# False because, is lower method returns True
# when string has only lower case letters
print(s.lower().islower()) # 
# True because, lower method makes every character
# in string lower case. 

str = "python "
print(str.islower()) #True

str.upper()

print(str.isupper()) # 
# False, because string is an immutable object
# therefore, it will not change its value unless 
# reassigned.

print(str.upper().isupper())
# True because upper method will make everything
# uppercase, since I chained upper and isupper
# method. 
















