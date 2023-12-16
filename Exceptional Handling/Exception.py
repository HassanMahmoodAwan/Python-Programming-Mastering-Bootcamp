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


# ===== Try-Except-Else clause ======
try:
    def func(a=10):
        if a < 5:
            b = a/(a-3)
        print(b)
    func(4)
    func(3)
except ZeroDivisionError:
    print('Zero Division')
else:
    print(b)

# ====== Try-Except-Else-Finally =======
try:
    def func(a=10):
        if a < 5:
            b = a/(a-3)
        print(b)
    func(4)
    func(3)
except ZeroDivisionError:
    print('Zero Division')
else:
    print(b)
finally:
    print('Always Excecuted')


# ======= Manually Raise Error ======
try: 
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    

# ======= Manually Raise Error, guess difference ======
try: 
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise