# Type Conversion

a = 2     # INTEGER
b = 4.25  # FLOAT
sum = a + b  # As float is greater than integer, the result will be float i.e. 2.0 + 4.25 = 6.25
print(sum)
# -----------------------------------------------------------------------------------------------------------------

# c = "2"  # STRING
c = int("2")  # Type Casting from string to integer

d = 4.25 # FLOAT
print(type(c))
print(type(d))
# print(c + d)  # This will give an error as we cannot add string and float

#But we can convert the string to float and then add it to float ---->This is called Type Casting.

print(c + d)


#-----------------------------------------------------------------------------------------------------------------
p = 3.14
p = str(p)  # Type Casting from float to string
print(type(p))

