name = input("Enter your Name: ")
print("Welcome ",name,"✨")


# Always gives String as Data Type
value = input("Enter some value : ")
print(type(value), value)  # This will give <class 'str'> as output

#To assure that their is correct data type we can use Type Casting to convert the string to integer or float.

val = int(input("Enter some value : "))
print(type(val), val)

print("-----------------------------------")

name = input("Enter your Name:")
age = int(input("Enter your Age:"))
marks = float(input("Enter your Marks:"))
print("Name:",name)
print("Age:",age)
print("Marks:",marks)
print(type(name),type(age),type(marks))