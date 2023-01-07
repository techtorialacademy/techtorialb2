
# Create a string variable

a = "hello"       #12345
#  first letter in hello
b = "hello " # 123456
             # hello 

# How do we compare these two strings? 

# We can use == sign to compare two string values. 

print(a == b) # False

c = "Hello"

print(a == c) # False, because the cases of the 
# strings are important. 

print(a == "hello") # True

print('hello' == "hello") # True

# String is one of the built in data types in python
# And string values are immutable, they don't change
# their value unless reassigned. 


# In the code you want to create an email template
# 

email_template = ''' Hello Techtorial,

I will not be able to attend class today, because
of some personal reasons. 

Thanks, 
Name LastName

'''

print(email_template)

















