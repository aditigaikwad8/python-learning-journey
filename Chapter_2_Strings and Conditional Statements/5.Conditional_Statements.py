'''
Conditional Statements

if-elif-else statements are used to perform different actions based on different conditions. 
They allow you to control the flow of your program by executing certain blocks of code only when specific conditions are met.

Here's a basic structure of an if-elif-else statement in Python:

if condition1:
    # Code to execute if condition1 is true
    pass
elif condition2:
    # Code to execute if condition2 is true
    pass
else:
    # Code to execute if none of the above conditions are true
    pass 

'''

age = 16

if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

light = "green"

if light == "red":
    print("Stop! The light is red.")
elif light == "yellow":
    print("Caution! The light is yellow.")
else:
    print("Go! The light is green.")


'''
It always checks the first condition, if it is true, it executes the code block under it and skips the rest of the conditions. 
If the first condition is false, it moves on to check the next condition (elif), and so on. 
If none of the conditions are true, it executes the code block under else.
but elif allows you to check multiple conditions in sequence. 
You can have as many elif statements as you need, and they will be checked in order until one of them evaluates to true. 
If none of the conditions are true, the else block will be executed.
and elif checks when if the previous if or elif conditions were false. 
It allows you to check additional conditions without having to nest multiple if statements, 
making your code more readable and organized.

'''

num = 5

if (num > 2):
    print("The number is greater than 2.")
if (num > 3):
    print("The number is greater than 3.")

# Output will be both statements because both conditions are true. 
# However, if you use elif instead of the second if, only the first condition will be checked, and the second condition will be skipped if the first one is true.

num = 5

if (num > 2):
    print("The number is greater than 2.")
elif (num > 3):
    print("The number is greater than 3.")

# In this case, only the first statement will be printed because the first condition is true, and the second condition will not be checked.

# Else is run when all the previous conditions are false. It acts as a fallback option when none of the specified conditions are met.


#'    ' this space is called indentation before  print in each if,elif,else block.