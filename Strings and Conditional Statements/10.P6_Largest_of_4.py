# WAP to find the largest of 4 numbers entered by the user.

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
num3 = int(input("Enter Num3: "))
num4 = int(input("Enter Num4: "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4 ):
    print("The greatest of 4 numbers is: ",num1)
elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("The greatest of 4 numbers is: ",num2)
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
    print("The greatest of 4 numbers is: ",num3)
else:
    print("The greatest of 4 numbers is: ",num4)