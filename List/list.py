"""
There are build-in 4 Data Structures in Python
    1- List
    2- Dictionary
    3- Tuple
    4- Sets

List are Ordered, Mutable Collection. Duplicate are allowed. All data types are allowed.


Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). (geeksforgeeks)


I learned that list are like LinkedList and Numpy_array is an actual array

"""



def list_basic():

    # creating a list using its constructor.
    fruits = list(("Apple", "Banana", "Orange"))
    print(fruits)
    print(fruits[1])
    # Normal way of creating.
    vegetable = ["onion", "tomato", "potato", "garlic"]
    print(vegetable)

    print(len(fruits), type(vegetable))

    if "Apple" in fruits:
        print("yes its in the list")
    else:
        print("its not in the list")

    # Checking Mutability of list
    fruits[2] = 'peach'   # Deep Copy
    print(fruits)


def list_slicing(vegetable=None):

    if vegetable is None:
        vegetable = ["onion", "tomato", "potato", "garlic"]

    print(vegetable[2:4])
    print(vegetable[:8])
    print(vegetable[2:])
    print(vegetable[:])
    print(vegetable[-10:-1])
    print(vegetable[:-1])


def two_d_list(list_2d=None):
    if list_2d is None:
        list_2d = [['Geeks', 'For'], ['Geeks']]

    # Accessing 2d-List Elements
    print(list_2d[0][0])


def list_advance_operations(list_2d=None):
    # Inserting into List

    if list_2d is None:
        list_2d = [['Geeks', 'For'], ['Geeks']]
    # if index more than the existed one then putted it on last.
    list_2d.insert(3,'Hello Geeks for Geeks')
    # inserting multiple values in one index
    list_2d.insert(1, [10, 15])

    # Appending into List (means putting at last)
    list_2d.append(21)
    print(list_2d)

    # Reversing a List
    reversed_list = list_2d.reverse()  # returning None, why?
    print(reversed_list, list_2d)

    revers = reversed(list_2d)  # returns Iterator, so convert it to list
    print(list(revers))

    # Using Slicing, reversing a List
    reverse_list = reversed_list[::-1]
    print(reverse_list)


def list_comprehension():
    # list comprehension take less time than traditional way.

    numList = [num**2 for num in range(10)]
    evenList = [num**2 for num in range(20) if num%2 == 0]
    print(evenList, numList)

    # Matrix creation using Comprehension  (2_D)
    matrix = [[j for j in range(4)] for i in range(3)]
    print(matrix)


if __name__ == '__main__':
    # list_basic()
    # list_slicing()
    list_advance_operations()
    # list_comprehension()
