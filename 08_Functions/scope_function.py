# Scope of Variables
"""
When working with vairable in Functions, variables are divided with respect to different scopes.

    - Local Scope:
        Variable declare inside Function, cannot access from outside. But availble for inside function.
    
    - Global Scope:
        Declare in main body of Python Code. 


Naming Variables:
    Operate with the same variable name inside and outside of function, Python treat them as two separate variables.

Global Keyword:
    If needed global variable, but are stuck in local scope, you can use the global keyword.

"""

# ===== Local Scope =====

def myfunc():
    x = 300
    print(x)
myfunc()


def my():
  x = 300
  def myinnerfunc():
    print(x)            # as Inner Func, global Scope.
  myinnerfunc()

my()




# ===== Global Scope =====

x = 300

def myfun():
  print(x)

myfun()
print(x)



# ===== Naming Variable =====
x = 300             # Global Scope

def myfunc():
  x = 200           # Local Scope
  print(x)

myfunc()

print(x)



# ===== Global Keyword =====
def myfunc():
  global x
  x = 300

myfunc()
print(x)


x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)

