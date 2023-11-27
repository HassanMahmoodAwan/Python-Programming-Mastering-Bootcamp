"""
Operators are used for performing Mathematical Operations as well as for Comparison between different variables.
            We have three main types of Operators

    Arithmetic Operations:      +, -, *, /, %, **, //(only give Integer part).
    Logical Operation:         and, not, or. (returns Boolean).
    Relational Operations:     >, <, !=, ==, <=, >=, <<, >>. (returns Boolean).

Note: Use for Comparison between variables or constant and we use it for decision-Making.
"""

a, b = 10, 12

print(a < b, a != b, a == b, a << b, not (a > b))  # relational Op, In binary we left shift b times in a.
a += 2
print(a)  # (a+=2) == (a= a+2)




