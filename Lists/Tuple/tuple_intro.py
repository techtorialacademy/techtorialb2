
# How can I create tuple with one item in it?

tupl = ("class")  # This is not a tuple
print(type(tupl)) #-> this line will print <class 'str'>

tl = ("class",) # This makes it a tuple with one element

print(type(tl))

# How do we access the elements from tuple?

t = ("c","b","d",1,2,3,4)
# print all elements in this tuple in a different line? 
for y in t:
    print(y)

# Do negative indexes work for tuple as well? 
# Yes, it does.
print("Negative index 5 is ",t[-5])

#Range of indexes (Slicing)

t = ("c","b","d",1,2,3,4)

print(t[2:5]) #"d",1,2

print(type(t[2:5])) # tuple

print(type(t[-4])) # <class 'int'> 
print(type(t[-5])) # <class 'str'>

print(t[2:3]) # ("d",)
print(type(t[2:3])) # Tuple


# "2" is not equal to 2 in python
# "2" is equal to "2"
# 2 is equal to 2


# How could we check if certain items exist in a tuple?


t = ("c","b","d",1,2,3,4)

if "d" in t:
    print("d is in the tuple")
else:
    print("d is not in the tuple")

print("d" in t) # True
print("d" not in t) # False



print(2 in t)  # True
print(2 not in t) # False



t = ("c","b","d",1,2,3,4)
#Line below will generate a type error.
# t[2:6] = ("new1","new2","new3","new4")

print(t) 










