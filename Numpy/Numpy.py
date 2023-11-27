"""
Numpy is an array which is the alternative of List in python.
    Way much powerful then List and have lots of buildin functions which helps to execute lots of functionalities in less code.


Note: Used to Handle two dim Arrays or Vectors like gray scale Images.

We will be Learning About:
    1- Numpy Array
    2- Slicing of Numpy
    3- Operations
    4- Advance way of creation and Splitting
    5- Stacking and Concatenation
    6- Numpy File Creation
    7- BroadCasting

"""

# Importing Numpy
import numpy as np


# Developing a Numpy Array.
def numpy_array():
    List = [10, 12, 14, 2, 0, 15]
    arr = np.array(List)

    print(arr)
    print(arr.shape)
    print(type(arr))



def array_slicing(arr):
    print(arr[2:-1])
    print(arr[:2])
    print(arr[::])  # Guess the Answer


def numpy_operations(arr):
    # Operations
    operations = [arr.sum(),
    arr.mean(),
    np.sin(arr),
    np.sum(arr),
    arr.reshape(6, ),
    arr.flatten(),   # Test on 2-D array.
    np.sign(arr),
    np.std(arr),
    np.cos(arr),
    np.shape(arr) ]

    for operation in operations:
        print(operation)


def advance_numpy_operations(arr):
    # Advance Concepts

    print(np.split(arr, 3))  # Splitting: same partition. Note: 3 new np arrays.

    # creating a new array.
    arr1 = np.random.randint(low=0, high=10, size=(2, 4))  # Keyword Argument
    print(arr1)

    arr2 = np.random.randint(0.0, 10.0, (2, 4))  # Positional Argument. Not Prefer
    print(arr2)

    # creating new 1-d array using arrange keyword.
    arr3 = np.arange(9).dtype
    print(arr3, type(np.arange(9)))
    arr3 = np.arange(2, 9)
    print(arr3)
    arr3 = np.arange(0, 10, 2)  # If not possible gap, it skip it
    print(arr3)
    # help(np.arange(9).dtype)

    print(type(arr3))
    print(arr3.dtype)


def numpy_stacking_concatenation():
    # Concatenation
    arr01 = np.array([10, 22, 1, 0, 16])
    arr02 = np.arange(2, 12)
    concatenate_result = np.concatenate((arr01, arr02))
    print(concatenate_result)

    # Stacking  such as vertical & Horizontal

    arr03 = np.random.randint(low=0, high=10, size=(2, 4))
    arr04 = np.random.randint(low=0, high=20, size=(2, 4))

    verticalStacked = np.vstack((arr03, arr04))
    horizontalStacked = np.hstack((arr03, arr04))
    print(horizontalStacked, "\n\n", verticalStacked)

    # Stacking over different rows and (vstack: rows not matter,  hstack: col not matter)

    arr5 = np.array([[7, 11, 15, 14], [3, 5, 6, 10], [10, 34, 234, 2]])  # 3x4
    arr6 = np.array([[2, 1, 15, 14], [3, 5, 6, 10]])  # 2x4
    arr7 = np.array([[2, 1], [3, 5], [4, 8]])  # 3x2

    verticalStacked = np.vstack((arr6, arr5))
    horizontalStacked = np.hstack((arr5, arr7))
    print("\n\n\n", verticalStacked, "\n\n", horizontalStacked)

    # Stacking using Concationation (Axis  0 for rows(vstack), 1 for colS(hStack))
    verticalStacked = np.concatenate((arr5, arr6), axis=0)
    horizontalStacked = np.concatenate((arr7, arr5), axis=1)
    print("\n\n\n", verticalStacked, "\n\n", horizontalStacked)


# Creating Numpy File and understanding Reshaping Rule.
def numpy_file():
    arr5 = np.array([[7, 11, 15, 14], [3, 5, 6, 10], [10, 34, 234, 2]])
    np.save("array.npy", arr5)

    importedArray = np.load("array.npy")
    print(importedArray)

    reshapedArray = arr5.reshape(4, 3)  # does not affect original (deep copy)
    print(reshapedArray)


# Scaler and Dynamic BroadCasting of Numpy Array
def numpy_broadcasting():
    # Rule: if one matching and other side is 1 or zero then Possible.

    a = np.array([[2, 3, 1], [2, 4, 5]])  # 2x3
    b = np.array([[2, 3, 1]])  # 1x3

    print(a + b)

    b = np.array([[2], [8]])  # 2x1
    print(a + b)

    # (5,3,1) + (1,1,1) possible
    # (5,3,1)+ (4,1,1) possible
    # (5,3,1)+ (1,3) possible


if __name__ == '__main__':
    List = [10, 12, 14, 2, 0, 15]
    arr = np.array(List)

    choice = int(input('Enter your Choice: '))

    match choice:
        case 1:
            numpy_array()
        case 2:
            array_slicing(arr)
        case 3:
            numpy_operations(arr)
        case 4:
            advance_numpy_operations(arr)
        case 5:
            numpy_stacking_concatenation()
        case 6:
            numpy_file()
        case 7:
            numpy_broadcasting()
        case '_':
            print('Enter the Correct value of Choice')

