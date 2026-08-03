print ()
print("=== Scholarship Eligibility Checker ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
attendance = int(input("Enter attendance percentage: "))
discipline = input("Do you have disciplinary issues? (yes/no): ").lower()

print ()
print ("=" * 40)
print ()

if age >= 18:
    print("Age requirement satisfied.")
else:
    print("Age requirement not satisfied.")

if score >= 70:
    score_ok = True
    print("Score requirement satisfied")
else:
    score_ok = False
    print("Score requirement not satisfied.")
attendance_ok = attendance >= 60
age_ok= age >=18
discipline_ok = discipline == "no"

print("Has no discipline issues" if discipline_ok else "Has discipline issues")
print("Attendance above minimum requirement" if attendance_ok else "Attendance below minimum requirement.")
if score_ok and attendance_ok and discipline_ok and age_ok:
    print(name, "is eligible for the scholarship.")
    bonus = score + 5
    print("Bonus Score:", bonus)
else:
    print(name, "is NOT eligible for the scholarship.")
