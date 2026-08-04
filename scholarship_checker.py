print ()
print("=== Scholarship Eligibility Checker ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
attendance = int(input("Enter attendance percentage: "))
discipline = input("Do you have disciplinary issues? (yes/no): ").lower()
if discipline != "yes" and discipline != "no":
    print("Invalid input for disciplinary issues. Please enter 'yes' or 'no'.")
    exit()

print ()
print ("=" * 40)
print ()


age_ok = age >= 18
score_ok = score >= 75 and score <= 100

attendance_ok = attendance >= 80 and attendance <= 100

discipline_ok = discipline == "no"

if age_ok and score_ok and attendance_ok and discipline_ok:
    print(name, "is eligible for the scholarship.")
elif discipline_ok == False:
    print(name, "is NOT eligible for the scholarship due to disciplinary issues.")
else:
    print(name, "is NOT eligible for the scholarship.")


