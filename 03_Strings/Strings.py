"""
String is an Array of Characters.
 which actually consist of characters, symbols, 0-9, special symbols.

If we not assign string to variable then python ignore it. like this multi-comment.

Note: Strings are immutable which mean not Changeable.

we will see
    - String variable
    - length of String
    - Combining of two String
    - Strings Slicing
    - String Manipulation Operations


Note: By default, input return  string from user. To take Number, float, boolean we need TypeCasting

"""

name = "Hassan"

print(name)
print(name[0])  # give 'H'
print(len(name))  # give length of String
print(name + " " + "Mahmood")  # Combine Both and Print

print("Has" in name)  # returns Boolean value after checking substring 'Has' in String as Strings are Arrays.   (Mapping Operator)

# Escape Characters :: As see earlier.
print("my name is \"Hassan Mahmood\"")
print("My marks are 80\\100")

# String Slicing
fruit = "Alphonso Mango"
print(fruit[2:4])  # ph as 4 ignored  :: Last not Consider
print(fruit[:8])  # Starting till 8th index, 8th index not Included.
print(fruit[2:])  # From index 2 to Last
print(fruit[:])  # Consider All
print(fruit[-10:-1])  # onso Mang
print(fruit[:-1])  # Give all except Last

# String manipulation Operations
degree = """  Bachelors in Computer Science   """

print(degree.upper())
print(degree.lower())
print(degree.capitalize())
print(degree.title())
print(degree.replace(" ", '_'))
print(degree.strip())  # Trim the String
print(degree.strip().split(" "))  # split string in a List. Chain Function

# To combine string and Number we use Format() same as f before string.
string = "my age is {}"
age = 21
print(string.format(age))

print(degree.index("he"))  # return first occurrence in form of index.
print(degree.find("he"))  # same as index.
print(degree.count("a"))  # No of char 'a' in a string

# String are Immutable
country = 'Pakistan'
location = 'Lahore, '
location += country
print(location)  # it works

# but
location = 'Punjab, Pakistan'  # possible
# location[0] = 'N'     # not possible as immutable.

# Note: Only can reassign whole string not single character.


# Congratulations! you learn about Strings.
