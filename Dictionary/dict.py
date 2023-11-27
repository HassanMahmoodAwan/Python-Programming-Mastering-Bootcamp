"""
There are build-in 4 Data Structures in Python
    1- List
    2- Dictionary
    3- Tuple
    4- Sets


Dict:
    No duplicate, mutable and ordered collection.
    key value pair
    It's related to Hash Tables as in Hashing It contains the key:value pair.

Its like Object in Javascript and like a JSON format.
Note: Very useful Data Structure as help in storing data, transferring data through API


"""


def dictionary():
    # Creating the dict using Constructor
    student_dict = dict(names='ABC', sections="B")

    section = {
        "Name": "Hassan",
        "Roll No": "Sp20-Bcs-114",
        "Section": "FA20-BCS-B",
        "Subject": "Artificial Intelligence"
    }
    print(section["Name"])

    # Input using the student.
    student = {}
    for i in range(2):
        name = input("Enter the name of student: ")
        semester = input("Enter the Semester of Student")
        student[name] = semester
    print(student)

    # Nested Dictionary
    nested_dict = {1: ['Geeks', 'learn'], 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
    print(nested_dict)
    print(nested_dict[3]['B'])  # Guess ???


def dict_func():
    # Dict Update Function
    student = dict([('Hassan', 7), ('Ali', 10)])
    updated_list = {'Hamid': '6'}
    student.update(updated_list)
    print(student)  # Merge both dict.

    # Using Get Method
    print(student.get('Hamid'))

    # Del method
    del student['Ali']   # will del this key-value pair


def advance_dict_func():
    dict1 = {1: "Python", 2: "Javascript", 3: "Mojo", 4: "Java"}

    # copy()  # Now manipulation on dict2 not affect dict1
    dict2 = dict1.copy()
    print(dict2)

    # clear() :: erase all items (key-value pair)
    dict1.clear()
    print(dict1)

    # items() :: give all items. check the format of return
    print(dict2.items())

    # return keys()
    print(dict2.keys())

    # pop() the given key value
    dict2.pop(4)
    print(dict2)

    # popitem() pop from the last
    dict2.popitem()
    print(dict2)

    # return all values()
    print(dict2.values())


def dict_comprehension():
    keys = ['a', 'b', 'c', 'd', 'e']
    values = [1, 2, 3, 4, 5]

    dict_declare = {k: v for (k, v) in zip(keys, values)}

    dict_coding = {x.upper(): x * 3 for x in 'coding'}
    print(dict_coding)


if __name__ == '__main__':
    # dictionary()
    # dict_func()
    dict_comprehension()