# Create a function that returns average of numbers from given list.
# When we are calculating the average we shouldn't include 
# largest and smallest element in the array. 
# If the largest or smallest number duplicated just not use one copy
#
# [10,12,10,12] -> 11
# 12 + 7 + 9 + 3 -> 31 / 4 -> 7.75
# [ 7,9] 
# [12,7,9,3] -> 8

def avg(l):
    # if I use sort method largest element will be at the end, smallest
    # element will be at the beginning of the list. 
    l.sort()
    # l[0] -> will be the smallest element
    # l[len(l)-1]-> will be the largest element
    sum = 0
    for index in range(1,len(l)-1):
        sum+=l[index]
    return sum / (len(l)-2 )

print(avg([12,7,9,3]))