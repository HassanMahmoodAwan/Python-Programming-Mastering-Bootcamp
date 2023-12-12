"""
We have two types for Conditional Statements
    1- IF-ELSE
    2- Match-Case

Both use for Decision-Making and checking the Condition.

Note: we will discuss Match-Case here (Not much use as limited Options).

Note: Developing a Result Evaluation App in terms of CGPA.


"""

eachSubjectMarks = 100
mathMarks = int(input('Enter the Math Marks: '))
programmingMarks = int(input('Enter the Programming Marks: '))
web_developmentMarks = int(input('Enter the Web Development Marks: '))
machine_learningMarks = int(input('Enter the machine Learning Marks: '))

totalObtainedMarks = mathMarks + programmingMarks + web_developmentMarks + machine_learningMarks

averageMarks = totalObtainedMarks / 4

CGPA = 'Not Assign'

match averageMarks:
    case range(90, 101, 1):            # Not working
        print('4.0')
    case 20:
        print('fail')
    case _:
        print('not solved')

# How to solve this problem using match case. Check it.
