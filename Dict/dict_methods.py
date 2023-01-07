#.values(), .keys()

d1 = {
	"brand":"Apple",
	"model":"Macbook Pro",
	"year" :2021
}


print(d1.values())
print(type(d1.values()))#<class 'dict_values'>

print(d1.keys())
print(type(d1.keys()))#<class 'dict_keys'>


# To get all values from the dict

for v in d1.values():
    print("Value of v is",v,"data type of v is",type(v))



