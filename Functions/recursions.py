
# Factorial of the numbers
# factorial numbers multiplied from 1 to n
# factorial 5 is 1 * 2 * 3* 4 * 5
# Factorial 0 and 1 is equal to 1
# 5 factorial is equal to 5 times 4 factorial
# 4 factorial is 1*2*3*4 -> * 5 -> 5!
# n times n-1 factorial will give us n factorial
# 7 times 7-1 factorial will give us 7 factorial
# 3 times 3-1 factorial will give us 3 factorial
# product of the numbers till the number n
# 7 factorial -> 1 * 2 * 3 * 4 * 5 * 6 * 7

def factorial(n):
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)  
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# since the factorial 1 is 1
# 5 * 4 * 3 * 2 * 1


























