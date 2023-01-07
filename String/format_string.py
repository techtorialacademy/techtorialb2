
first_exam = 70
second_exam = 90
third_exam = 78

# I want to create a string variable 
# where I can display all grades of this student. 

str = "First exam score is {},second exam score is {},third exam score {} "

print(str.format(first_exam,second_exam,third_exam))
#First exam score is 70,second exam score is 90,third exam score 78 


str = "First exam score is {2},second exam score is {1},third exam score {0}"

print(str.format(first_exam,second_exam,third_exam))
#First exam score is 78,second exam score is 90,third exam score 70 











