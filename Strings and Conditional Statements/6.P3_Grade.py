'''
Grade students based on marks

marks >= 90, grade = "A"

90 > marks >= 80, grade = "B"

80 > marks >= 70, grade = "C"

70 > marks, grade = "D"

'''

marks = float((input("Enter your Marks: ")))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->", grade)