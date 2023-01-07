# In the factory we need to create a program that can 
# find if we can do the shipment and if we can do the shipment
# it will tell us how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 

# count of small package = 4 -> 4 kilogram
# count of big package = 1 -> 5 kilogram 
# goal is to ship 9 kilogram 
# i can ship and i need to use 4 small package

# 5 small package-> i need to use 3 smal package
# 4 big package  -> how many big package i need to use -> 2
# I need to ship 13 kilogram 
# i can ship and i need to use 3 small package

# 3 small package-> i need to use 4 small package to complete but since i don't 
# have 4 small package i cannot ship
# 3 big package -> i can use max 2 big package
# i need ship 14 kilogram
# I cannot ship

print("Enter the kilogram amount of shipment")
goal_ship = int(input()) # 32

print("Enter amount of small packages you have")
count_of_small = int(input()) # 

print("Enter amount of big packages you have")
count_of_big = int(input()) # 6
# Big package is 5 kg and small package is 1 kg


# How many big packages do we need to use to achieve this goal?
#                      29
big_packages_needed = goal_ship // 5 #  -> 5



# # I can have two conditions
# # We have enough big packages, and we don't
# if count_of_big < big_packages_needed:
#     kg_I_have = count_of_big * 5
#     needed_small_packages =goal_ship - kg_I_have
#     # There is still 2 conditions, either I have small packages i need to ship or i don't
#     if count_of_small >= needed_small_packages:
#         print(f"I can do the shipment and  I need {needed_small_packages} small packages")
#     else:
#         print("I can't do the shipment because,")
#         print(f"I need {needed_small_packages} small packages but, I have {count_of_small} package")    
# elif count_of_big >= big_packages_needed:
#     # How can I find how many small package I need?
#     small_package_needed = goal_ship % 5
#     # There is still 2 conditions, either I have small packages i need to ship or i don't
#     if count_of_small >= small_package_needed:
#         print(f"I can do the shipment and  I need {small_package_needed} small packages")
#     else:
#         print("I can't do the shipment because,")
#         print(f"I need {small_package_needed} small packages but, I have {count_of_small} package")    










# The way you say it I am allowed to over the shipment goal as long as 
# it is not more 5 kg
  
if count_of_big >= big_packages_needed:
    # How can I find how many small package I need?
    small_package_needed = goal_ship % 5
    # There is still 2 conditions, either I have small packages i need to ship or i don't
    if  2< small_package_needed or small_package_needed>count_of_small:
        went_over = 5-small_package_needed
        goal_ship = goal_ship+ went_over
        big_packages_needed= goal_ship//5
        print("I can do the shipment because,")
        print(f"We didn't have enough small package so we went over {went_over}")
        print(f"And we used {big_packages_needed} big packages")
    elif small_package_needed <=count_of_small:
        print(f"I can do the shipment and  I need {small_package_needed} small packages")

elif count_of_big < big_packages_needed:
    kg_I_have = count_of_big * 5
    needed_small_packages =goal_ship - kg_I_have
    # There is still 2 conditions, either I have small packages i need to ship or i don't
    if count_of_small >= needed_small_packages:
        print(f"I can do the shipment and  I need {needed_small_packages} small packages")
    else:
        print("I can't do the shipment because,")
        print(f"I need {needed_small_packages} small packages but, I have {count_of_small} package")  




