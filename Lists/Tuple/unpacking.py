
obj_in_cl = ("camera","table","light","laptop","screen")

# Line above is called packing a variable in python.

# we can also unpack the variables in tuple


# How many elements does the tuple above has?
#5
item1,item2,item3,item4,item5 = obj_in_cl
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)


###
obj_in_cl = ("camera","table","light","laptop","screen")

# I want to unpack these variables with 3 variable total
i1, i2, *i3 = obj_in_cl

print(f"The value of i1 is {i1} and the data type of i1 is",type(i1))
print(f"The value of i2 is {i2} and the data type of i2 is",type(i2))
print(f"The value of i3 is {i3} and the data type of i3 is",type(i3))

obj_in_cl = ("camera","table","light","laptop","screen","ttt")

t1, *t2,t3,t4 = obj_in_cl

print(f"The value of t1 is {t1} and the data type of t1 is",type(t1))
print(f"The value of t2 is {t2} and the data type of t2 is",type(t2))
print(f"The value of t3 is {t3} and the data type of t3 is",type(t3))









