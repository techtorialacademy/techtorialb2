set1 = {1,2,4}
set2 = {"b","d","f"}
set3 = set1.union(set2)
print(set3)
print(set1)
print(set2)

set1 = {1,2,4}
set2 = {2,"4",1}
set3 = set1.intersection(set2)

print(set3) #{1,2}

set1 = {1,2,4}
set2 = {2,"4",1}

set3 = set1.symmetric_difference(set2)

print(set3)