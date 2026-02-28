# Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).


student_score = 99

if student_score > 100:
    print(f"\nPlease verify your grade again.\n"
          f"Your score {student_score} is greater than 100.\n")
    exit()

if student_score < 0:
     print(f"\nPlease verify your grade again.\n"
          f"Your score {student_score} is less than 0.\n")
     exit()
     
if student_score >= 90:
    grade = "A"

elif student_score >= 80:
    grade = "B"

elif student_score >= 70:
    grade = "C"

elif student_score >= 60:
    grade = "D"

else:
    grade = "F"

print(f"Grade: {grade}\n")