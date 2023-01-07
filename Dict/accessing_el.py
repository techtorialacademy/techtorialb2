d1 = {
	"brand":"Apple",
	"model":"Macbook Pro",
	"year" :2021
}

# how can you access the values from this dict?

#Using the value of the keys we can acces the elements

print(d1["brand"]) # -> Apple
print(d1.get("brand")) # -> Apple

# print(d1['new']) # -> Key error because 'new' is not present in the map
print(d1.get("new")) # None
# The difference between accessing the element using get method or 
# square brackets is when square brackets used and key is not present in 
# the dictionary it will generate an Key Error. However,in get method
# we won't see this error even key is not present in the dictionary.

