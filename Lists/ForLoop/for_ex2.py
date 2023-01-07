# Create a program that will ask user ten full name 
# After you get 10 full name create email version of given 10 
# name and store it inside list and print. 
#enter fullname
# John Wick
#enter fullname
# Max White
#["johnwick@gmail.com","maxwhite@gmail.com",.....]

# I need to ask user 10 full name 
# I need a loop that'll iterate 10 times
# range(10) -> how many numbers this range object contains?
list_mails = []
for i in range(10): # this loop will iterate 10 times
    print("enter a full name")
    full_name = input()
    email = full_name.lower().replace(" ","")+"@gmail.com"
    list_mails.append(email)
print(list_mails)



