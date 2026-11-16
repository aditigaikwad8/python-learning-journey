str1 = "This is a sample string."
str2 = 'This is another string.'
str3 = """This is a multi-line string.""" 

# This is becoz Python allows you to use either single quotes or double quotes to define strings. The choice between them is often a matter of personal preference or convenience, especially when the string itself contains quotes.
# For e.g., if your string contains a single quote, you might prefer to use double quotes to define the string, and vice versa.
# e.g., str4 = "It's a beautiful day."  # Using double quotes to avoid conflict with the single quote in "It's"

# str = "This is a string.
# We are creating in python."

# We can see in above example 2nd line string is giving an error...For that we use ESCAPE SEQUENCE CHARACTERS.

str = "This is a string.\n We are creating in python."
print(str)  # Output: This is a string. We are creating in python.
# \n is an escape sequence that represents a new line character. When the string is printed, it will create a line break at that point.

str4 ="This is a string with a tab character.\tWe are creating in python."
print(str4)  # Output: This is a string with a tab character.    We are creating in python.


# BASIC STRING OPERATIONS
# 1. Concatenation: You can concatenate (combine) strings using the + operator
str5 = "Hello, "
str6 = "World!"
print(str5 + str6)  # Output: Hello, World!

# 2. Length of String
str7 = "Hello, World!"
print(len(str7))  # Output: 13

#-------------------------------------------------
str8 = "Hello"
str9 = "World"
final_str = str8 + "    " + str9  # Concatenating with a space in between
print(final_str)  # Output: Hello World
print(len(final_str))  # Output: 11


print("***INDEXING***")

str10 = "Hello World"
ch = str10[0]  # Accessing the first character
print(ch)  # Output: H
print(str10[5]) # Output: W

# but if we try to change the character at a specific index, we will get an error because strings are immutable in Python.
# str10[0] = 'h'  # This will raise an error

print("***SLICING***")
str11 = "Hello World"
print(str11[0:4])  # Output: Hell
print(str11[6:11])  # Output: World
print(str11[6:len(str11)])  # Output: World
print(str11[6:])  # Output: World
print(str11[:5])  # Output: Hello [0:5] means from index 0 to 4 (5 is not included)
 

# Negative Indexing: In Python, you can also use negative indexing to access characters from the end of the string. The last character has an index of -1, the second last character has an index of -2, and so on.

str12 ="Apple"
print(str12[-3:-1])  # Output: pl
print(str12[-5:-2])  # Output: App

