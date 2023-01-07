# Given a string, return a version where all 
# the “x” have been removed.
# Except an “x” at the very start or
#  end should not be removed.
# “xxHxix” → “xHix”
# “abxxxcd” → “abcd”
# “xabxxxcdx” → “xabcdx”
print("Enter any word")
str = input()

first_letter = str[0]
last_letter  = str[-1]
# I need to get part of string without first and last letter. 
middle = str[1:-1 ]

converted = first_letter + middle.replace("x","") + last_letter

print(converted)


