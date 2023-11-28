"""
Operators are used for performing Mathematical Operations as well as for Comparison between different variables.
            We have four main types of Operators

    - Arithmetic Operations:      +, -, *, /, %, **, //(only give Integer part).
    - Logical Operation:         and, not, or. (returns Boolean).
    - Relational Operations:     >, <, !=, ==, <=, >=, <<, >>. (returns Boolean).
    - Mapping Operations:        'has' in 'hassan', not in.

Arithmatic Operators are used for computations of variables or constants.
    BDMAS rule is follow for solving Equation: So precedence is as follows:

        Precedence:
            1- Expressions between parentheses
            2- Exponents
            3- Multiplication and division (from left to right)
            4- Addition and subtraction (from left to right)

Note: % give use Remainder   13 % 2 ->  guess the Answer ?
"""

a, b = 10, 12  # a=10, b=12
mathEq = (1200 - 10) // 14 * ((12) - 100)  # Equation of Constant Values
print(mathEq)

# Another Example with variables is give as
eq = (a - 1200) ** 2 // 18 + (b % 2)  # guess the Answer.
print(eq)

# Percentage gives use the Remainder
print(b % 5)