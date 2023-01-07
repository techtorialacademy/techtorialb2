# Ask user to give two string values and 
# print True if the second string starts with 
# last two charachters 
# of the first string OR print True 
# if the first string starts with
# first two charachters of the second string.

print("enter first string")
s = input()

print("enter second string")
s2 = input()
 
# I need last 2 characters of the first string
last_two = s[-2:]

condition1 = s2.startswith(last_two)

# I need to find first 2 characters of the second string
first_two = s2[:2]
condition2 = s.startswith(first_two)

print(condition1 or condition2)

























