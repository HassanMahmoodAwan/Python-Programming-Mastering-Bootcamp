"""
- Loops have a lot of importance in programing.
- Iterating over list, dict, or running a problem multiple times is actually done using loops.

- Loops are actually repeating some Code for certain No of Iterations.

Types of loops in Python:
    1- For Loops
    2- While Loops
    3- Nested Loops

- Else statement can be used with Loops, when condition fullfil.


Loop Control Statement:         # Check out by you own.
    - Continue
    - break
    - Pass

"""

# Simple For Loop.
for i in range(0, 4): 
    print(i) 


# === List Iteration ===
List = ["geeks", "for", "geeks"] 
for i in List: 
    print(i)


# === Dict Iteration ===
Dict = dict(name='Hassan', age='22')

for key in Dict:
    print(f'{key} = {Dict[key]}')

for key, value in Dict.items():
    print(key, value)


# === Tuple Iteration ===
Tuple = ("geeks", "for", "geeks") 
for i in Tuple: 
    print(i)  


# === Set Iteration ===
Set = {1, 2, 3, 4, 5, 6} 
for i in Set: 
    print(i)


# ELSE block in For Loop
List = ["geeks", "for", "geeks"] 
for index in range(len(List)): 
    print(List[index]) 
else: 
    print("Inside Else Block") 


# === Enumerator ===
List = ['Deep', 'Mind', 'Algo']
for index, value in enumerate(List):
    print(index, value)



# === Zip in For Loop ===
List01 = ['Deep', 'Mind', 'Algo']
List02 = ['StartUp', 'Company']

for i in zip(List01, List02):
    print(i)                    # Return Tuple, Ignore Unmatching



# ===== Exception Handling with Loops ======
fruits = ["apple", "orange", "kiwi"] 
iter_obj = iter(fruits) 
while True: 
    try: 
        fruit = next(iter_obj) 
        print(fruit) 
    except StopIteration: 
        break