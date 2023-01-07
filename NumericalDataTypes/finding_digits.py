
a = 538
# The number a can be any three digit number.
# Solution should work for every three digit number.
# Multiply the each digit of number a

# When we integer divide number with 10 it will get rid of 
# the last digit of the number. 

# When I find remainder with 10 I get the last digit of the number. 

# multiplication = a%10 * (a//10%10) * (a//100)
# print(multiplication)

last_digit = a % 10 

first_two_digits = a // 10

middle_digit = first_two_digits % 10

first_digit = first_two_digits //10

print("Multiplication of each digit of number a is",(first_digit
*last_digit*middle_digit))



# Create a function to find each digit of the given number. 
# Create a program to find each digit of the number and sort them. 
# Creat e program to find each prime digit of the number. 






















