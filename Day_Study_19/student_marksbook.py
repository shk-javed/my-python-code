students = {}

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Update Marks")
    print("4. Show All")
    print("5. Show Topper")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        marks = int(input("Marks: "))
        students[name] = marks
        print("Added!")

    elif choice == "2":
        name = input("Name to remove: ")
        if name in students:
            del students[name]
            print("Removed!")
        else:
            print("Not found!")

    elif choice == "3":
        name = input("Name to update: ")
        if name in students:
            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks
            print("Updated!")
        else:
            print("Not found!")

    elif choice == "4":
        print(students)

    elif choice == "5":
        if students:
            topper = max(students, key=students.get)
            print(f"Topper: {topper} ({students[topper]} marks)")
        else:
            print("No students present!")

    elif choice == "6":
        break

    else:
        print("Invalid choice")
