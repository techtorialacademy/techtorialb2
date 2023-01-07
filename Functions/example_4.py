# Create a method to check if a given string is palindrome.
# Palindrome string means when the string equals its reversed version.
# hannah, civic etc.
# How can I make this method not case sensitive
def is_palindrome(s1):
    reversed = s1[ ::-1]
    reversed = reversed.capitalize()
    s1 = s1.capitalize()

    return reversed == s1

print(is_palindrome("string")) 
print("Techtorial"[:-1])
print("Techtorial"[::-1])