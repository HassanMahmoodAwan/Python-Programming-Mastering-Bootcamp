"""
Operators are used for performing Mathematical Operations as well as for Comparison between different variables.
            We have three main types of Operators

    Arithmetic Operations:      +, -, *, /, %, **, //(only give Integer part).
    Logical Operation:         and, not, or. (returns Boolean).
    Relational Operations:     >, <, !=, ==, <=, >=, <<, >>. (returns Boolean).

Note: Result of Logical Operator is always a Boolean Value on which we can take decisions.
"""

a, b = 10, 12
# Run and See the Result.
print(a and b == 10, a or b == 10, not a, not (not a))  # Logical Operations.

print(bool(not "Hassan"))  # returns False

# Making Decision based on Logical Operator Result.
if not(a >= 20) and b >= 5:
    print('You get the Access.')
