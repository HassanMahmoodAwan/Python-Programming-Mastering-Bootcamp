"""

Tuples:
    - Tuples are Immutable -> cannot change,
    - Ordered, Duplicated Allowed.
    - Indexing.
    - All DataTypes Allowed

Note: Similar to List like Duplications, Iterations, all DataType, Nested-Tuples  but Immutable. 

"""


# ==== Tuple Development ====
var = ("Geeks", "for", "Geeks"); print(var)

# ==== Using Constructor ====
t1 = tuple(('DSA', 'OOP', 'Web-Development', 'Data-Science'))
print(t1)

# ==== Using Python 3.11 =====
Tuple: tuple[int | str, ...] = (1,2,3,'GeeksforGeeks', 'DeepMindAlgo')
# Note: only str and Int allowed, ... means multiple
print(Tuple, type(Tuple), len(Tuple))


# ======= Guess Tuple or Not =======
Tuple = ('Python',);     print(type(Tuple))
notTuple = ('Python');   print(type(notTuple))


# ==== Checking Imutability ====
mytuple = (1, 2, 3, 4, 2, 3)
# mytuple[1] = 100                      # Not Allowed
mytuple: tuple[int, ...] = (10,2,6)     # Allowed



# ==== Concatnating ====
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
print(tuple1 + tuple2)


# ==== Nested Tuple ====
tuple3 = (tuple1, tuple2);      print(tuple3)


# ==== Repition in Tuple ====
tuple3 = ('python',)*3
print(tuple3)


# ==== Reversing Tuple ====
print(tuple1[::-1])