# Ask user to give you a string
# Ask user to give order number of the letter and
#  print that letter from the string
# I have the positon of the letter
# 
print("Please enter any text")
str = input()

print("""Please enter order number of the letter 
you want to see""")
order_num = int(input())

# user doesn't know index numbers in python.
# The order number that user will give me
# will be one bigger than the index number of letter.
index_num = order_num - 1

print(str[index_num])







