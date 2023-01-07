# Create a python program to give 
# most efficient exchange possible using only 
# coins 
# quarter 25 cent
# nickel 5 cents
# dime is 10 cents
# penny 1 cent
# $2.34 exchange
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies
# create a program to give a change using least coin possible.
exchange = 0.52

# from the given amount of exchange how many quarter can i give  ? 
# I will convert exchange to cents
total_cents =  exchange * 100
# 1 dollar is 100 cents
# 1 quarter is 25 cents
count_of_q = total_cents // 25 # 2
print(count_of_q)

# I give enough quarters, however how can I complete rest of the 
# exchange? 
# I have to check what is left over after i gave the quarters. 
# To find the left overs after giving quarter
left_after_quarter = total_cents % 25

# i have to find how many dimes I can give it back
count_of_dimes = left_after_quarter // 10

# I have to find what is left over after giving dimes
left_after_dimes = left_after_quarter % 10

# I have to find how many nickel I can give.
count_of_nickel = left_after_dimes // 5

count_of_pennies = left_after_dimes % 5


print("For $",exchange, "I will give",count_of_q," quarters"
, count_of_dimes," dimes", count_of_nickel, " nickels", count_of_pennies,
"pennies")






