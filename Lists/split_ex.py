
# Find how many word does the given string contain?
# "techtorial academy" -> 2
# "python is a proggramming language" -> 5

# space is seperating words from each other.

print("Enter a sentence")
sentence = input()

lis = sentence.split(" ")

print(lis)
count_of_words = len(lis)
print(count_of_words)

# Second Solution
#Count of words in a given string can be found by finding 
# count of spaces + 1

count_of_spaces = sentence.count(" ")
print("Comes from count of space +1 ",count_of_spaces+1)

















