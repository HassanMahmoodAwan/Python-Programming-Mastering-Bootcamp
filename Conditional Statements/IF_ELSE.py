"""
We have two types for Conditional Statements
    1- IF-ELSE
    2- Match-Case

Both use for Decision-Making and checking the Condition.

Note: we will discuss IF-ELSE here (Most popular).

Note: Developing a Result Evaluation App in terms of CGPA.
"""

eachSubjectMarks = 100
mathMarks = int(input('Enter the Math Marks: '))
programmingMarks = int(input('Enter the Programming Marks: '))
web_developmentMarks = int(input('Enter the Web Development Marks: '))
machine_learningMarks = int(input('Enter the machine Learning Marks: '))

totalObtainedMarks = mathMarks + programmingMarks + web_developmentMarks + machine_learningMarks

averageMarks = totalObtainedMarks / 4


CGPA: str = 'Not Assign'

if averageMarks > 100:
    print('Invalid Input Given')
elif averageMarks >= 90 and averageMarks < 100:
    CGPA = 4.0
elif 85 <= averageMarks < 90:
    CGPA = 3.7
elif 80 <= averageMarks < 85:
    CGPA = 3.3
elif 75 <= averageMarks < 80:
    CGPA = 3.0
elif 70 <= averageMarks < 75:
    CGPA = 2.7
elif 65 <= averageMarks < 70:
    CGPA = 2.3
elif 60 <= averageMarks < 65:
    CGPA = 2.0
elif 55 <= averageMarks < 60:
    CGPA = 1.7
elif 50 <= averageMarks < 55:
    CGPA = 1.3
else:
    CGPA = 'You Failed in  this Semester'


# Displaying the Answer
print(CGPA)