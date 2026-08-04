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

attendance_ok = attendance >= 60

discipline_ok = discipline == "no"

if age_ok and score_ok and attendance_ok and discipline_ok:
    print(f"{name}is eligible for the scholarship.")
else:
    print(f"{name}is NOT eligible for the scholarship.")
    print("Reason(s):")
    if not age_ok:
        print("Must be at least 18 years old.")
    if not score_ok:
        print(f"Score ({score}) is below the required 75.")
    if not attendance_ok:
        print(f"Attendance ({attendance}%) is below the required 80%.")
    if not discipline_ok:
        print("Disciplinary issues on record.")

#Bonus score is not needed
#If statememnts for age waas not needed
#Age was not used as a requirement in the final checking for eligibility
