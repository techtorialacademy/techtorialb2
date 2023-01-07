#Print the pattern below using loop
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# We won't use list to solve

# i need numbers from range 1 to 5 inclusive
# Outer loop will help us to get line number
for i in range(1,6):
    s = ""
    # inner loop helps us to get how many number we should add to the 
    #string variable
    for x in range(1,i+1): # How many times this loop is going to iterate?
        # It is going to iterate i times.
        # THis range object will start from one and will go till the i
        s = s+" "+ str(x)
    print(s)    
