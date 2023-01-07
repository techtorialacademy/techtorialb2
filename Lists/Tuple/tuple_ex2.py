
a = (2,3,5,7,10,11,0,1)

# Sort this tuple and print out the result. 

# Value of the tuples can't be changed, neither order nor value. 

# if I have list I can sort it
# I have currently a tuple, but i need a list
# Is there a possibility that I can convert(cast) tuple to list?
# function list() will convert(cast) tuple object to a list object?

l = list(a)
for index in range(len(l)):
    #list[index]
    for n in range(index+1,len(l)):
        if l[index] > l[n]:
            save_the_valueoflistIndex = l[index]
            l[index] = l[n]
            l[n] = save_the_valueoflistIndex

# My end result shoul be stil in tuple type
# Using function tuple() list can be converted in to tuple object

l =tuple(l)
 
print(l)
print(type(l))





















