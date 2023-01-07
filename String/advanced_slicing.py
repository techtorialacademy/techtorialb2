#    012345
#         
s = "python"

print(s[-1]) #n

# index -1 will always give the last letter 
# from the string. 

print(s[-3])

print(s[-4 : -1]) # tho

print("This line",s[-4:-6]) # There is no letter in this scope

print(s[3:1]) # There is no letter in this scope


str1 = "Python is an object oriented"

print(str1[1:15:3])

# in slicing when there is 3 arguments
# first one is starting index
# second one is ending index
# third one is step 

# What do you think will happen when the step 
# number is negative? 

city = "Chicago"

print(city[::-1]) # Will reverse string.

# Ask user to enter any integer number and 
# print that number reversed. 

print("Enter any integer number")

number = input()

print(number)

reversed_num = number[::-1]

print(reversed_num)
print("Data type of this number is",type(reversed_num))

# In 2 argument slicing what happened?

s = "Techtorial"
print(s[4:2]) # Nothing

# In 3 argument slicing when the step is negative

print(s[4:2:-2]) #th
















