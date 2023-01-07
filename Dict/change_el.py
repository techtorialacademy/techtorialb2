d1 = {
	"brand":"Apple",
	"model":"Macbook Pro",
	"year" :2021
}
#I want to change the model of the laptop
d1["model"] = "Macbook Air"
print(d1)

# Adding new element to a dictionary
d1["new"] = "Macbook Pro"

print(d1) #{'brand': 'Apple', 'model': 'Macbook Air', 'year': 2021, 'new': 'Macbook Pro'}

# Can I change the elements in different way?
#update method to change value of elements in a dictionary
# update method takes a dictionary as parameter and changes the value
# of element

d1.update({"year":2022})
print(d1)

# Adding new element to a dictionary
d1.update({"charging-port":"usb"})
print(d1)




