list = [2,5,True,"s",2.5]

#print(list[5]) # IndexError: list index out of range

print(list[2]) # True

print(type(list[3])) # <class 'str'>

print(list[1:4]) # 5, True, s

# We are getting range of elements fromt the list
# Therefore it will be another list.
print(type(list[1:4])) # 
#list = [2,5,True,"s",2.5]
list[1:2] =["new1","new2"]
#[2,,True,"s",2.5]
# [5] =["new1","new2"]
#[2,"new1","new2",True,"s",2.5]
print(list[2]) # new2
print(type(list[1])) # <class 'str'>
print(type(list[0])) #<class 'int'>

list = [2,5,True,"s",2.5]
list[1] = ["new1","new2"]

print(type(list[1])) #<class 'list'>
#[2,,True,"s",2.5]
# 5 = ["new1","new2"]
#[2,["new1","new2"],True,"s",2.5]


print(list[1][0]) # new1

print(list[-1])
print(len(list)-1)

print(list[-1])