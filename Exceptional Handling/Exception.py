"""
- Error in Python can be of two types:
    1- Syntax ERROR
    2- Exception

Exception occur when Internal even stop flow of program.

"""

# ====== Basic Exception ========
try:
    a = 10
    b = '20'
    c = a+b
except TypeError:
    print('Both need to be Int.')


# ====== Multiple Exception =======
try:
    def func(a):
        if a < 4:
            b = a/(a-3)
        print(b)

    func(3)
    func(5)
except ZeroDivisionError:
    print('Not divide by zero')
except NameError:
    print('variable not exist')