# The doctors say  babies can go out in summer if the weather is 
# between 60 and 80 inclusive. If not they say you shouldn't take the baby out. 
# In the winter they say you can go out if the weather is hotter than -20
#Ask user what season they are in also ask user how hot the weather 
# is  and print if they can go out with baby or not. 

print("What is the season now? ")
season = input()
print("How hot is the weather currently?")
degree = int(input())
# First solution
if 60<=degree<=80 and season == "summer":
    print("you can take the baby out")
elif season == "winter" and degree>-20:
    print("you can take the baby out")
else:
    print("you cannot take the baby out")
    
#Second solution

if season == "summer":
    if 60<=degree<=80:
        print("you can take the baby out")
    else:
        print("You cannot take the baby out")
elif season =="winter":
    if degree>-20:
        print("I can take the baby out")
    else:
        print("I cannot take the baby out")    




















