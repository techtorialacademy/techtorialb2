
# create a method to find highest common factore of two given numbers.
# highest common factor is a biggest common divisor of two given numbers.
# 24 18 -> 6
# 32 12 -> 4
# 24 12 -> 12 

def highest_common_factor(n1,n2):
    # if it can divide both numbers without any remainder
    hcf = n1
    while n1%hcf != 0 or n2 % hcf != 0:
        hcf = hcf - 1
    return hcf

print(highest_common_factor(18,24))








