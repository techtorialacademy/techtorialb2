
list = [0,2,5,11,100,6,200,1]

# Create a program that will sort this list,
# without using a sort method.


# I have to find place of each element 
# acorrding to value of all other elements

# Zero is smaller than 1 therfore it has to come before element 1.


for index in range(len(list)):
    #list[index]
    for n in range(index+1,len(list)):
        if list[index] > list[n]:
            save_the_valueoflistIndex = list[index]
            list[index] = list[n]
            list[n] = save_the_valueoflistIndex

print(list)










