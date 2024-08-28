# Q1: Run For loop infinite time.

def infinte_loop() -> int:
    infinite = float('+inf')
    for i in range(0, infinite):
        print('Hello World!')
    
    return 0

# There is no way in python to represent infinte Integer. Without integer, range will not work.


# Q2: Change the count variable value on which loop is excecuting.
def count_changer() -> int:
    count: int = 10
    for i in range(0, count):
        print('Hello World!')
        count += 1

    print(count)

if __name__ == '__main__':
    count_changer()