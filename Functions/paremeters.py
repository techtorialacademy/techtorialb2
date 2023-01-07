
# Create a method that takes full name as parameter
# and returns upper case version of that fullname.

def upper_case_name(full_name):
    return full_name.upper()


# Since int object doesn't have upper method 
# the code below will return 'int' object has no attribute upper()
#print(upper_case_name(5))

print(upper_case_name("John Wick"))

#The code below will generate a type error,because our method
# can take only one parameter at a time.
#print(upper_case_name("John Wick","Saul Goodman"))

print(upper_case_name("Saul Goodman"))

print(upper_case_name("Yusuf Turan"))

# When the methods are created we can call it as many times as 
# necessary

