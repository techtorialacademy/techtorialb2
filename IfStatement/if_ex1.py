# getting ticket for speed violation
#   in state of IN, speed limit on HighWays is 70  
#   in other states, speed limit on Highways is 55
#   -if driver exceeds speed limit for up to 10% of the limit in each state, 
#    we will give WARNING in that state
#     state of IN warning means --> print --> "YELLOW WARNING"

#     other state warnings mean --> print --> "CITATION"
# -if driver exceeds speed limit more than 10% of the limit in each state,
#  we will give TICKET in that state
#     state of IN ticket means --> print --> "$150 and 5 points"
#     other state ticket means --> print --> "$100"
# -if speed is same as  speed limit or lower, --> print --> "You are driving safe!"
limit_IN = 70 #0.1 * 70 + 70 -> 77
limit_US = 55
print("Please enter your state")
state_of_driver = input()

print("Please enter speed of driver")
speed_driver = int(input())

is_in_IN = state_of_driver == "IN"

if (is_in_IN and speed_driver<=limit_IN) or (not is_in_IN and speed_driver <=limit_US):
    print("You are driving safe!")
elif is_in_IN and speed_driver<=(limit_IN+0.1*limit_IN):
    print("YELLOW WARNING")
elif not is_in_IN and speed_driver<=(limit_US+ 0.1*limit_US):
    print("CITATION")
elif is_in_IN and speed_driver>(limit_IN+0.1*limit_IN):
    print("$150 and 5 points")
elif not is_in_IN and speed_driver>(limit_US+ 0.1*limit_US):
    print("$100")  


