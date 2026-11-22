str ="i am a studing Python programming language."

print(str.endswith("age."))  # Output: True Here, endswith() method checks if the string ends with the specified suffix "age." and returns True if it does, otherwise it returns False.
print(str.capitalize())  # Output: I am a studing python programming language. Here, capitalize() method capitalizes the first character of the string and converts the rest of the characters to lowercase.
print(str) #Here, we are printing the original string to show that the capitalize() method does not modify the original string, but instead returns a new string with the desired capitalization.

# If you want to modify the original string, you can assign the result of the capitalize() method back to the original variable like this:
str = str.capitalize()
print(str)  # Output: I am a studing python programming language. Now, the original string has been modified to have the first character capitalized and the rest of the characters in lowercase.

print(str.replace("studing", "learning"))  # Output: I am a learning python programming language. Here, replace() method replaces all occurrences of the substring "studing" with the substring "learning" and returns a new string with the replacements made.
print(str.replace("studing","✨✨✨✨✨✨"))

print(str.find("o"))  # Output: find() method returns the index of the first occurrence of the substring "o" in the string. If the substring is not found, it returns -1.
print(str.find("python"))  # Output: 14 Here, find() method returns the index of the first occurrence of the substring "python" in the string. If the substring is not found, it returns -1.
print(str.find("Python"))  # Output: -1 Here, find() method returns -1 because the substring "Python" is not found in the string. The find() method is case-sensitive, so it does not match "Python" with "python".

print(str.count("a"))  # Output: 2 Here, count() method returns the number of occurrences of the substring "a" in the string.

