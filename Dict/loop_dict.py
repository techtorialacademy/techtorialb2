# Using for loop we can all key names in dict
d1 = {
	"brand":"Apple",
	"model":"Macbook Pro",
	"year" :2021
}
# The loop below will print all key names in dict.
for k in d1:
    print(k)
# print all values in the dict?
# d1[keyname] what will this give it to you? 
# it will give you value for the keyname
for k in d1:
    print(d1[k])


# We can get key and value at the same time using loop
# We need to use items method

for k,v in d1.items():
    print("Key is",k,"and value is",v)









