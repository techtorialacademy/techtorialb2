list =[1,5,6,11,90,3,6]

#Print all the odd numbers from index number 3 to 6 inclusive
# We need all elements from index 3 to 6 inclusive

# I need index numbers ranging from number 3 to 6 inclusive.
# range(3,7)

for e in range(3,7):
    #What is the way that i can check if list[e] is odd or not?
    if list[e] % 2 !=0:
        print(list[e])
