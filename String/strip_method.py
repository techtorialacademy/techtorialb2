
# We can ask user to enter a string and 
# remove the spaces in the beginning and at the 
# end of the string. 

str = "       Techtorial          "

print(str)
print(str.strip())


# In strip method we can provide a character
# and it will remove that character from the beginning
# and end of the string. 

#  Let's write a phone number in the middle of 
#  hashtags

phone_num = "####2247778888###"

print(phone_num.strip('#'))

# we can use strip method with multiple characters
# as well. 

web_site = "www.techtorialacademy.com"
# I want to get domain name

print("Domain name of this website is ",
 web_site.strip("owmc."))






