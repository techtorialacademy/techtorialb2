str = "object oriented Programmingo"

l = str.split("o")
#-> "", "bject ", "riented Pr","gramming"
print(l)


s = "techtorial academy"
l2 = s.split("a")

print(l2)
# -> "techrori","l ","c","demy"

# The seperator cannot be empty
# l3 = s.split("")
# print(l3)


l4 = s.split("z")
print(l4)



s = "techtorial academy"

l5 = s.split("al")

print(l5) # -> ['techtori', ' academy']