
import csv

students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100")
        return

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    students.append({
        "name": name,
        "marks": marks,
        "grade": grade
    })

    print("Student added successfully!")

def show_students():
    for student in students:
        print(student)

def show_ranking():
    ranked = sorted(
        students,
        key=lambda s: s["marks"],
        reverse=True
    )

    for position, student in enumerate(ranked, 1):
        print(position, student["name"], student["marks"])

def save_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "marks", "grade"]
        )
        writer.writeheader()
        writer.writerows(students)

    print("Data saved successfully!")

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Show Ranking")
    print("4. Save CSV")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        show_ranking()
    elif choice == "4":
        save_csv()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
