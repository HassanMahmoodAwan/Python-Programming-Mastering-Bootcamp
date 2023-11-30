"""
There are build-in 4 Data Structures in Python
    1- List
    2- Dictionary
    3- Tuple
    4- Sets

List: 
    List are Ordered, Mutable Collection. Duplicate are allowed. All data types are allowed.


Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). (geeksforgeeks)


I learned that list are like LinkedList and Numpy_array is an actual array

"""



def list_basic():

    #  ==== using Constructor. =====
    fruits = list(("Apple", "Banana", "Orange"))
    print(fruits, fruits[1])

    # ===== Normal way =====
    vegetable = ["onion", "tomato", "potato", "garlic"]
    print(len(vegetable), type(vegetable))

    # ==== Mapping Operator ====
    if "Apple" in fruits:
        print("yes its in the list")
    else:
        print("its not in the list")


    # ==== Mutability of list =====
    fruits[2] = 'peach'   # change orignal.
    fruits[1:2] = ['Apricot', 'Stawbery']
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

    # ==== Practice Question ===== : wanted to prind  all ato.
    count = 0
    for element in vegetable:
        if element[-3:] == 'ato':
            count += 1
    print(count)


def two_d_list(list_2d=None):
    if list_2d is None:
        list_2d = [['Geeks', 'For'], ['Geeks']]

    # Accessing 2d-List Elements
    print(list_2d[0][0])




def list_advance_operations(list_2d=None):
    if list_2d is None:
        list_2d = [['Geeks', 'For'], ['Geeks']]
    

    # ===== Inserting =====
    # if index more than existed, then putted it on last.
    list_2d.insert(3,'Hello Geeks for Geeks')
    # Note: Can Insert one val Using Insert.
    list_2d.insert(1, [10, 15])


    # ===== Apending =====
    list_2d.append(21); print(list_2d)


    # ===== Extending List ======
    list_2d.extend([2,3,5]); print(list_2d)


    # ===== Remove and Pop ======
    list_2d.remove(3)
    list_2d.pop(1)
    list_2d.pop()

    # ===== Del and Clear =====
    # del list_2d
    # clear(list_2d)          

    # ===== Reversing a List =====
    reversed_list = list_2d.reverse()  # returning None, why?
    print(reversed_list, list_2d )     # list_2d Reversed.

    revers = reversed(list_2d)  # returns Iterator,convert to list
    print(list(revers))

    # Reversing List using Slicing
    reverse_list = list(revers)[::-1]
    print(reverse_list)



def list_comprehension():
    # Note: list comprehension take less time than traditional way.

    numList = [num**2 for num in range(10)]
    evenList = [num**2 for num in range(20) if num%2 == 0]
    print(evenList, numList)

    # ==== Practice Question ====
    List = list((10, 12, 4, 6, 2))
    List = [element**2 for element in List]; print(List)

    # Matrix creation using Comprehension  (2_D)
    matrix = [[j for j in range(4)] for i in range(3)]
    print(matrix)


if __name__ == '__main__':
    list_basic()
    # list_slicing()
    # list_advance_operations()
    # list_comprehension()
