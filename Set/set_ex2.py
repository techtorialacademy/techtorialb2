import sys
s = [1,3,4,5,7]
s2 ={10,12,100,4,5}
#Find the second lowest element from the s and multiply with
# second highest element in the s2.

# The problem here is when the first element from the array is smallest
# This code wont' find second lowest element


lowest_s = sys.maxsize
# For second lowest I have to give so big number that
# any number in the array would have potential to change.
# sys.maxsize is a constant value that represents biggest integer number
# in python

second_lowest_s = sys.maxsize
print(second_lowest_s)

for el in s:
    if el<lowest_s:
        second_lowest_s =lowest_s
        lowest_s = el
    elif el < second_lowest_s:
        second_lowest_s = el
print(second_lowest_s)            
print("Lowest element in the list",lowest_s)

#Before I start the loop I have to give lowest value possible
# Lowest integer value in python is -sys.maxsize -1

largest_s2 = -sys.maxsize - 1
second_largest_s2 = -sys.maxsize -1

for element in s2:
    if element > largest_s2:
        second_largest_s2 = largest_s2
        largest_s2 = element
    elif element >second_largest_s2:
        second_largest_s2 = element
print(second_largest_s2)  

print("Result of multiplication is",second_largest_s2*second_lowest_s)