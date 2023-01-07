#We can use pop() method to remove elements with specified key value
d1 = {
	"brand":"Apple",
	"model":"Macbook Pro",
	"year" :2021
}
# We can remove the element
d1.pop("brand")
print(d1)
d1.update({"brand2":"Windows"})
print(d1)

# popitem() method
# it won't take any argument
# popitem() method will remove last inserted item in a dictionary.
d1.popitem()
print(d1)

# del keyword

del d1["model"]
print(d1)

#Removing all dictionary
#del d1
#print(d1) # Because object d1 is not present for python anymore

#empty all the dictionary

print(d1)
d1.clear() # Empty the dictionary so I will have empty dict 
print(d1) # {}