# Do-while Loop excecute at least one time.

counter: int = 1
roomNo: str = '221000'
while True:
    user_pass: int = int(input(f'Enter the  {counter} try Password: '))

    if user_pass == int(roomNo):
        print('You Unlock It')
        break

    if user_pass != int(roomNo) and counter > 5:
        print('Your Attempts Failed')
        break
    
    counter += 1
    continue


