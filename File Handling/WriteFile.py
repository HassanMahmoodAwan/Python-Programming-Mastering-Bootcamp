# ==== WRITE overide text in file ==== #
file = open('./data.txt', 'w')
file.write('Data overide')
file.close()


# ==== WRITE OTHER WAY ==== #
with open('./data.txt', 'w') as file:
    file.write('Again Overide file content')
    file.close()