"""
Variables are use for Storing data for use in Program.

Variables are of Many types:
    - Numeric: Numbers without Decimal Part..
    - Floats:  Numbers with Decimal Part.
    - Strings: Any Sentence or Words it can Also contain 0-9 but this     represents as sentence.
    - Boolean: Which are True or False.

Variables name Starts from Character and can have Numbers 0-9, _ , Characters.

Note: 
1- Use Camel Case for Variables (Preferred),
2- Lower Case for Function(), 
3- Upper Camel Case for Class(), 
4- Upper Case for constant


More we will learn Escape Characters  " \'vikings\' "
"""

name: str = 'Hassan'  # String    # Specifing DataType as well.
age: int = 20  # Int
cgpa = 2.71  # Float
student = True  # Boolean

# Can Store something for user Input.
lifeGoal = input('Enter your lifeGoal in one Word: ')  # camelCase used for initializing Variable

# Printing Variable
print(lifeGoal)

# Printing with Some Message and using two Variables
print(name + ' life Goal is: ' + lifeGoal)
print(name , " life Goal is: ", lifeGoal)

# Other way of printing same Line
print('{} life Goal is: {}'.format(name, lifeGoal))

# Another way given below
print(f'{name} of age {age} has life Goal: {lifeGoal}')

# ===== Lets now learn about Escape Characters  ======

print("We are the so-called \"Vikings\" from the north.")  # will give " ... "Vikings" ... "
print('22\\10')  # for using single Backslash \\
print(f"{name}\n{age}")  # New Line \n
print(f'{name}\t{cgpa}')  # One tab space \t


# Other Way of declaring Variables
name = "Hassan"; no1, no2, no3 = 10, 12, 8
numOne = numTwo = 22    # create shallow copy. changing one effects other.
print(name, no3, numTwo, type(numTwo))  # Type print int.

# Type Casting
strConvert = str(no2)
print(type(strConvert))
floatConvert = float(no1)
print(type(floatConvert))
str(numOne)
print(type(numOne))  # It creates a shallow copy.

# Congratulations! You learn variables, there use in Print, Input Statement. Also learn Escape Characters.
