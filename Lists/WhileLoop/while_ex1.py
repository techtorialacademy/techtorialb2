nums = [1,2,10,11,13,17,21,26]

#From the given list find sum of all the even numbers 
# lets find sum of all the odds seperately

# To be able to find all odd numbers in this list
# I have to check each number in the list and find which one is odd
# To be able to check each element I should start from index 0 
# go till the end of indexes.

index = 0
sum   = 0
while index <= len(nums)-1:
    # How do I access current element?
    # nums[index] -> current element in this iteration
    # I should check if this element is even or odd
    if nums[index] % 2 !=0:
        #This is an odd number
        sum = nums[index] + sum
    index += 1    

print(sum)         

