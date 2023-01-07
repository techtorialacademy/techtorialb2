# Create a method that will take one list as a parameter and one positive
# integer index as a parameter. Return the negative index for given
# positive index number. 

# We have to understand relation  between negative and positive indexes.
# [p,y,t,h,o,n]
#  0 1 2 3 4 5
#  6543     2-1 (negatives)
# positive index - len(string) will give us the negative index. 
def find_neg(s1,index):
    neg_index = index - len(s1)
    return neg_index
print(find_neg(["p","y","t","h","o","n"],3))    