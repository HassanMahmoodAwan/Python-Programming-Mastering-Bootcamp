"""
Set:
    - Unordered Collection
    - Non Duplicate
    - Mutable but not single element Assignment
    - All Data Type


Note: Simlar like we studied in Mathamatics. 


FrozenSet:
    - Frozen sets are immutable Set


Operations:
    - Union
    - Intersection
    - Difference
"""

# ==== Set ====
var = {"Geeks", "for", "Geeks"}
print(type(var))

# ==== Set using Constructor ====
myset = set(["a", "b", "c"]);  print(myset)

# ==== Mutability ====
myset.add("d"); print(myset)

myset[1] = "Hello"          # Not Allowed


# ==== Frozen Set ====
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)