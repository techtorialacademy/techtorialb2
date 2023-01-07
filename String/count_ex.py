# Ask user to give a string filled with cat and dog texts
# From the given string if the number of dogs 
# and cats  is the same print True,
#  other wise print False

print("Give a string consists of dog and cat words")
str = input()

count_of_dogs = str.count("dog")

count_of_cats = str.count("cat")

is_counts_same = count_of_cats == count_of_dogs

print(is_counts_same)












