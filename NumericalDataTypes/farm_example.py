# In the farm we have 35 cows , 23 chickens,
#and 40 ducks.
# Create a program to calculate total number of 
# legs in the farm
#Requirements create a variable for 
# cows, chickens and ducks , and create variables
#for their number of legs. 
# print "We have 'result' legs in the farm"

number_of_cows = 35
number_of_chickens = 23
number_of_ducks = 40

legs_of_cow = 4
legs_of_bird = 2

total_cow_legs = number_of_cows * legs_of_cow
total_duck_legs = number_of_ducks * legs_of_bird
total_chicken_legs = number_of_chickens * legs_of_bird

total_legs_of_animals = total_cow_legs + total_duck_legs + total_chicken_legs

print("We have",total_legs_of_animals,"legs in the farm")







