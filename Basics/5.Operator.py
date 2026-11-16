'''
 Operator is a symbol that performs a certain operation between operands.
 
 Here,
 a + b
 a and b are operands
'''
 
#Arithmetic Operators

a = 5
b = 2
# sum = a+b
# print(sum) 
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # Modulus ...Remainder
print(a ** b) # Exponentiation....a^b


#Relational Operators

x=50
y=20
print(x > y)  # Greater than
print(x < y)  # Less than
print(x == y) # Equal to
print(x != y) # Not equal to
print(x >= y) # Greater than or equal to
print(x <= y) # Less than or equal to

#Assignment Operators
c = 10
d = 5
# c = c + 10
c += 10
# BOTH ARE SAME ..c = c + 10---->c += 10
print("The value of c is :",c)

c-= 5
print("The value of c is :",c)
c*= 2
print("The value of c is :",c)
c/= 5
print("The value of c is :",c)
c%= 3
print("The value of c is :",c)
c**= 2
print("The value of c is :",c)


#Logical Operators
p = True
q = False
print(p and q) # Logical AND
print(p or q)  # Logical OR 
print(not p)   # Logical NOT