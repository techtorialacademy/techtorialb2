# Prime number
# prime numbers can only be divided by 1 and itself.
# 11 7 5 29 etc. 
# Every number can be divided by 1 and itself 
# but prime numbers cannot be divisible 
# by any other number than 1 and itself.
# Ask user to give you a range of numbers like starting and ending
# then find all the prime numbers in that range.
# starting from 2 to 20
# 2, 3, 5, 7, 11, 13, 17, 19 
# A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# A factor is a whole number that can be divided evenly into another number. 
# The first few prime numbers are 1, 3, 5, 7, 11, 13, 17, 19, 23 and 29. 
# Numbers that have more than two factors are called composite numbers.
print("Enter a starting point")
starting_num = int(input())
print("Enter ending point")
ending_num = int(input())

# I have to check every number in this range to understand if they 
# are prime number. 
# I have to check all possible dividers of a number 
# and other 1 and itself none of the possible divider should be able
# to divide that number to make it a prime number. 

# 11
# What is the possible dividers for this number 11?
# Every number that is smaller than 11 has a possibility to divide 
# that number
# for 11 which range should I look at the find possible dividers?
# 1 to 11
# for startin_num which range should I look at the find possible dividers?
# 1 to starting_num

# let's assume some values for starting and ending number
# starting_num is 12 ending_num 15
while starting_num <= ending_num:
    
    # instead of printing I have to find out if starting_num is prime.
    possible_divisor = 2
    # it should range from 2 to starting_num
    # I assume on the line below that starting number is a prime number
    is_prime = True
    while possible_divisor <starting_num:
        # I have to check if this possible divisor is an actual divisor of starting num
        if starting_num % possible_divisor == 0:
            is_prime = False
        possible_divisor +=1
    
    # THis line again belongs to outer loop
    if is_prime and starting_num>1:
        print(f"{starting_num} is a prime number")

    starting_num += 1


# I am able to get when the numbers are not prime
# I need to print only one time if they are prime or not.








