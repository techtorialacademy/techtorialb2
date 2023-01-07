nums = [1,2,3,1,2,3,4,2,2,2]






# Remove all the number 2's from this list.

# What is the index number of element 3? 2
# After the removal what is the index number of 3? 1
index = 0
# When I remove the element from the list I should not make an increase
# in the index number
while index < len(nums):
    if nums[index] == 2:
        nums.remove(2)
        index-=1
        
    index += 1    

print(nums)        



















