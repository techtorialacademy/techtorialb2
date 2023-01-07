# It will help us to get range of elements from the 
# string. 
# Syntax for using slicing.
# str[startingIndex:endIndex]

str = "Saturday"
#      01234567

print(str[2:5]) # tur

# Create a dynamic program to find middle three
# letters from given odd string. 
# "Chicago"  -> ica
# "seven"    -> eve
    #  0123456
str = "Chicago" # 
# For odd length string the middle index is 
# last index // 2 
last_index = len(str)-1
middle_index = last_index // 2

middle_three = str[middle_index-1 : middle_index+2]

print(middle_three)















