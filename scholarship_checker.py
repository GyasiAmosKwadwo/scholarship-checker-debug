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

# if age >= 18:
#     print("Age requirement satisfied.")
# else:
#     print("Age requirement not satisfied.")

# if score >= 70:
#     score_ok = True
# else:
#     score_ok = False

age_ok = age >= 18
score_ok = score >= 75

attendance_ok = attendance >= 80

discipline_ok = discipline == "no"

if age_ok and score_ok and attendance_ok and discipline_ok:
    print(name, "is eligible for the scholarship.")
else:
    print(name, "is NOT eligible for the scholarship.")
