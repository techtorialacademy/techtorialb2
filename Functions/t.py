print("enter three ingredients")
ingredients = input()
print ("enter any digit")
digit = int(input ())
first_space_index = ingredients.strip().find(" ")

first_word = ingredients [0 : first_space_index]
print(first_word)
second_space_index = ingredients.rfind(" ")
second_word = ingredients [first_space_index +1 : second_space_index]
third_word = ingredients [second_space_index+1 : 1]
#changing first letter of the first word
#remove the first letter of the first word and add the number #at the beginning of the string
first_word = str(digit) + first_word[1:1]
digit +=1
second_word = str(digit) + second_word [1:]
digit += 1
third_word = str(digit) + third_word[1:1]
print (first_word, second_word, third_word)