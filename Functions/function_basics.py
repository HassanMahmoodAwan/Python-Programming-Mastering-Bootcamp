"""
Python Functions is a block of statements that return the specific task. 

Some Benefits of Using Functions
    - Increase Code Readability 
    - Increase Code Reusability

Two types of functions in Python
    1- Built-in Function
    2- User-define Function

Types of Arguments in Functions
    - Default argument
    - Keyword arguments (named arguments)
    - Positional arguments
    - Arbitrary arguments (variable-length arguments *args and **kwargs)


Note: DocString is used to describe the functionality of the function.

NestFunctions: Functions with in Functions

Anonymous Functions:
    - function is without a name.
    - def keyword for normal Function but Lambda for Anonymous Functions. 

"""

# ======== Built-in Function ========
len('Full Stack Development')
career = 'Full Stack Development'
occurance = career.index('ll')



# ======= User Define Functions ========

# Simple Function
def fun():
    print("Welcome to GFG")
fun()


# Function with Argument
def even_odd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
even_odd(13)


# Function in Python3
def sum_num(no1: int, no2: int) -> int:
    result = no1 + no2
    return result
print(sum_num(20, 43))


# === Default argument ===
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)


# === Keyword Arguments ===
def student(firstname, lastname):
    print(firstname, lastname)
student(lastname='Practice', firstname='Geeks') # point to Note in it. Guess ???



# === Positional Arguments ===
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
nameAge("Suraj", 27)            # Position of Argument no change.


# === Arbitrary Keyword  Arguments === 
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# === **kwargs (return key-value pair) ===
def kwarg(**args):
    for key, value in args.items():
        print(key, value)
kwarg(first='Hassan', mid='Mahmood', last='Awan')


def kwargs_arg(**paras):
    for i in paras:
        print(i)
try:
    kwargs_arg('Hassan', 'Mahmood', 'Awan')
except KeyError:
    print('**kwargs take a dict as argument')
finally:
    print('Hope you Understand')


# === DocString Statement ===
print(even_odd.__doc__)         # __doc__  , Not working return None.