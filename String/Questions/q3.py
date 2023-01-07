# Given a string, return a new string made of 3 
# copies of the first 2 chars of the original string. 
# The string may be any length. 
# If there are fewer than 2 chars, 
# use whatever is there.
# "Hello" → "HeHeHe"
# "ab" → "ababab"
#"H" → "HHH"

# We can slice the first two chars out of the string
# and multiply the result by 3.
print("Enter string")
var = input()
first2 = var[:2]
result = first2 * 3
#result = first2 * 3 is same as result = first2 + first2 + first2
# to add a space between first2 -> result = first2 +" "+ first2+" " + first2
print(result)









