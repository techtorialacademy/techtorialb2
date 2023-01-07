
# Why do we use if statement? 
# For different conditions occur in the programming
# we might need to change our implementation.

# Python is a space sensitive language
# Indentation is 4 space, it shows which statement the implementation
# belongs. 

num1 = 16
num2 = 15
# Print num2 is bigger than num1 if num2 is bigger. 
if num1<num2:
    print("num2 is bigger than number1")
      
# Ask user to enter a string
# if user enters a string with all lower cases print
# you entered correct cases

print("Enter a string")
str = input()
# How can I check if all characters in string lower cases? 
# We can use islower() method, which returns a boolean value
#It returns true when all characters of a string are lower case. 

if(str.islower()):
    print("you entered correct cases")     #1
    print("because you entered all lower") #2
print("you entered a string")              #3
#   print("Is this line in the if? ")      #4

# Which of these lines above are effected by if statement ? 
# Line 1 and 2 are effected by if statement because of an indentation
# Line 4 will generate and indentation error,and line 3 will 
# get executed regardless of if condition.

# Elif 
# If the previous conditions are not true then elif statement
# will be checked.

var = "python"
if(var=="python"):
    print("value of the variable var is python")
elif(True):
    print("Value of var is not python")

# What will be the output of the code above? 
# "value of the variable var is python"












