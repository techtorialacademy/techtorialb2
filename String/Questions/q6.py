# Given two strings, append them together (known as "concatenation") 
# and return the result. However, if the strings are different lengths, 
# omit chars from the longer string so it is the same length as the 
# shorter string. So "Hello" and "Hi" yield "loHi". 
# The strings may be any length.



# if they are same length 
# I have to just do var + var2
#if they are in different length i have to omit chars
# from longer string
print("Enter a string")
str1 = input()
print("Enter a string")
str2 = input()
if len(str1) == len(str2):
    print(str1 + str2)
if len(str1) > len(str2):
    last_characters_str1 = len(str2)
    last_part_str1 = str1[-1*(last_characters_str1):]
    print(last_part_str1 + str2)
if len(str1) < len(str2):
    last_characters_str2 = len(str1)
    last_part_str2 = str2[-1*(last_characters_str2):]
    print(str1 + last_part_str2)