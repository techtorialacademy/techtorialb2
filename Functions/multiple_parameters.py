
# Let's create a function that takes multiple numbers 
# as a parameter and returns multiplication of those numbers.
# It could be 10 numbers or 4

def find_multiplication(*numbers):
    #This numbers variable should be treated as tuple, because it 
    # is a tuple
    multi = 1
    for element in numbers:
        multi *= element
    print(multi)    

find_multiplication(1,2,4,5,3)












