
'''
" List "

- Built-in datatype that stores set of values
- can store different datatype

'''
marks1 = 94.4
marks2 = 87.6
marks3 = 95.2
marks4 = 56.8
marks5 = 98.8

marks = [94.4, 87.6, 95.2, 56.8, 98.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

'''
In other language,arrays store data of  same data type.
While in Python ,List has no such rule.....can we have different datatypes.

e.g. 
student = ["Karan",75,"Delhi"]
'''
student = ["Karan",75,"Delhi"]
print(student)
print(student[0])
student[0] = "Arjun"
print(student) #List is Mutable

'''
Strings are immutable in Python
Lists  are Mutable in python 
Mutable means- that can change
Immutable means- that cannot change

'''

str = "hello"
print(str[0])
#str[0] = "y" # This can't be done as string is Immutable


