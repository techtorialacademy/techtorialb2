
txt = "I love apples, apple is my fruit."

count_apple = txt.count("apple")
print(count_apple)

# What if I am looking for an exact word apple
# not apples or pineapples

# We can add space at the beginning and end of the 
# word apple to distinguish from other words

count_apple_exact = txt.count(" apple ")

print(count_apple_exact)




