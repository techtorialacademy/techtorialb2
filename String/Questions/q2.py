# Given a string, print True if the first 2 
# chars in the string also appear at 
# the end of the string, such as with "edited".
# ed -> True
# edit -> False

print("Enter a string")
str1 = input()

# First 2 character and last 2 character should be 
# same
# I need to compare first 2 character and last 2 chars

# first2chars == last2chars

# How can I find first 2 and last 2 characters? 

first2chars = str1[:2] # first two chars 
#First solution is below
# last2chars = str1 [-2:]
# bl = first2chars == last2chars

#print(bl)

bl = str1.endswith(first2chars)

print(bl)

