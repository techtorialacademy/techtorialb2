# remove suffix -> will remove it from end of the string
# remove prefix will remove it from begginning of the string

s = "Hello World"

print(s.removeprefix("World")) # Hello World
# * underscore below means a space
print(s.removeprefix("Hello")) # _World

print(s.removesuffix("World")) # Hello_

print(s.removeprefix("olleH")) # Hello World

# Unlike the strip method, in remove suffix and prefix method
# order of the characters are important.
print(s.strip("elloH")) # _World

print(s.removeprefix("He")) # llo World
print(s.removesuffix("dl")) # Hello World
print(s.removesuffix("ld")) # Hello Wor





