# Ask user to give you two integer numbers. 
# Find the sum of these two integer numbers. 
# If sum of these two integer is smaller than 10 
# print sum of these two numbers is 10 
# if sum of these two number is between 10 - 19 inclusive, 
# print sum of these two numbers is 20
# For all other conditions 
# print the actual sum of these two numbers. 

print("Enter a number")
num1 = int(input())
print("Enter second number")
num2 = int(input())

sum_of_nums = num1 + num2

if sum_of_nums < 10:
    print("Sum of these two number is 10")
elif 10<=sum_of_nums<=19:
    print("Sum of these two numbers is 20")
else:
    print(f"Sum of these two number is {sum_of_nums}")        

# sum_of_nums>=10 and sum_of_nums<=19
# What happens when you multiple comparison operators consecutively?
# Python adds and automatically
# 10<=sum_of_nums<=19