# 1. Grade Calculator
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F (Fail)"

print("Your Grade is:", grade)
