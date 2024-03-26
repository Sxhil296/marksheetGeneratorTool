
print("*"*50)
print("Enter the details to generate the mark sheet.\n")

# take student's details
name = input("Enter the student's name: ").title()
roll_no = int(input("Enter the roll no: "))
enroll_no = int(input("Enter the enrollment no: "))
father_name = input("Enter students's father's name: ").title()
mother_name = input("Enter students's mother's name: ").title()
dob = input("Enter student's date of birth (DD/MM/YYYY): ")
gender = input("Enter the gender: ").title()
zip_code = int(input("Enter the zip code: "))
passing_year = int(input("Enter the passing year: "))
exam_board = input("Enter the board name: ").upper()
school_name = input("Enter the school name: ").title()

# subjects and marks list
subjects = ["Science", "Maths", "English", "SSt", "Hindi"]
grades = []
marks = []
max_marks = 100

for subject in subjects:
    marks.append(int(input(f"Enter the marks for {subject}: ")))
    # Calculate grades based on marks (example grading criteria)
    if marks[-1] >= 90:
        grades.append("A+")
    elif marks[-1] >= 80:
        grades.append("A")
    elif marks[-1] >= 70:
        grades.append("B")
    elif marks[-1] >= 60:
        grades.append("C")
    elif marks[-1] >= 50:
        grades.append("D")
    else:
        grades.append("F")

total_marks = len(subjects) * max_marks
marks_obtained = sum(marks)
percentage = marks_obtained / total_marks * 100
cgpa = percentage / 9.5


# Determine pass/fail status
# variable to count the number of subjects where the student has marks between 31 and 32
pass_count = sum(1 for mark in marks if 31 <= mark <= 32)
if pass_count == 1:
    pass_status = "Passed with Grace"
elif pass_count >= 2:
    pass_status = "Fail"
else:
    pass_status = "Pass"


# print the mark sheet
print("\n" + "*" * 50)
print("10th MARK SHEET\n")
print(f"Name: {name}")
print(f"Roll No: {roll_no}")
print(f"Enrollment No: {enroll_no}")
print(f"Father's Name: {father_name}")
print(f"Mother's Name: {mother_name}")
print(f"Date of Birth: {dob}")
print(f"Gender: {gender}")
print(f"Zip Code: {zip_code}")
print(f"Passing Year: {passing_year}")
print(f"Board: {exam_board}")
print(f"School: {school_name}\n")
print("SUBJECTS\tGRADES\tMARKS\tMAX_MARKS")

for subject, grade, mark in zip(subjects, grades, marks):
    print(f"{subject}\t\t{grade}\t{mark}\t{max_marks}")

print(f"\nTotal Marks Obtained: {marks_obtained}/{total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.2f}")
print(f"Pass/Fail Status: {pass_status}")



