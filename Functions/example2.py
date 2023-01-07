
# Create a method that will return
#  lowest common multiplication of two given numbers
# lowest common multiplication is lowest number that can be divided by
# given two numbers

# lcm for 4 and 6 is 12 
# 4 and 8 lcm is 8
# for 6 and 8 -> 24

def lcm(n1, n2):
    # we need to start from either n1 or n2 and we should increase the
    # number till we can divide
    lowest_c = n1
    # because i want to increase if these two numbers cant divide
    while (lowest_c%n1 !=0 or lowest_c%n2 !=0):
        lowest_c+=1
    return lowest_c
print(lcm(4,6))    
















