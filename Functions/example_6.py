# Create a method that takes one dict and one value as parameter.
# check if the given value exist in the dictionary.
# If the given value exist in dictionary return True, return False.

def is_value_present(dict,value1):
    #How can i get all the values from dictionary?
    #.values()
    return value1 in dict.values()

def is_key_present(dict,key1):
    #How can i get all the values from dictionary?
    #.values()
    return key1 in dict.keys()

d = {
    "name": "y",
    "last_name":"t",
    "school_num":390,
    

}
print(is_key_present(d,"n"))
print(is_value_present(d,390))
print(is_value_present(d,210)) 
print(is_value_present(d,"t"))