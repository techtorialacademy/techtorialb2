# Ask user to enter a string
# if the given string contains any duplicated letter
# print string has duplicated letter 
# otherwise print string consists of unique letters. 

print("Enter a string")
str = input()

# I have to check count of each letter in the string. 
# If any count of the letter is bigger than 1, it means 
# this string has duplicated letter. 
# java
index = 0
# On the line below I assume string doesn't have any duplicated letter
is_duplicated = False
while index < len(str):
    print(str[index])
    # my goal is to find if str[index] is unique or duplicated
    if str.count(str[index])> 1:
        is_duplicated = True
    index += 1    

if is_duplicated:
    print(f"{str} contains duplicated letters")
elif not is_duplicated:
    print(f"{str} doesn't contain any duplicated letter")       





















