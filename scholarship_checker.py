print ()
print("=== Scholarship Eligibility Checker ===")

full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your score: "))
attendance = int(input("Enter attendance percentage: "))
discipline = input("Do you have disciplinary issues? (yes/no): ").lower()

discipline_ok = discipline == "no"
is_eligible = age and score and attendance and discipline_ok

print ()
print ("=" * 40)
print(f"Student: {full_name}")
print()

if is_eligible:
    print("Status: ELIGIBLE")
    print()
else:
    print("Status: NOT ELIGIBLE")
    print()


if age >= 18:
    print("\u2714 Age requirement satisfied.")
else:
    print("X Age requirement not satisfied.")

if score >= 75:
    print("\u2714 score requirement satisfied.")
else:
    print("X Score requirement not satisfied.")
    
if attendance >= 80:
    print("\u2714 Attendance requirement satisfied.")
else:
    print("X Attendance requirement not satisfied.")

if discipline == "no":
    print("\u2714 Discipline requirement satisfied.")
else:
    print("X Discipline requirement not satisfied.")
print()  

if is_eligible:
    print(full_name, "is eligible for the scholarship.")
else:
    print(full_name, "is NOT eligible for the scholarship.")
print()

bonus = score - 5
print("Bonus Score:", bonus)