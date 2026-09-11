students = []

while True:

    print("\n========== STUDENT DATA ORGANIZER ==========")
    print("Press 1 for Add a Student")
    print("Press 2 for View All Students")
    print("Press 3 for Search a Student")
    print("Press 4 for Update a Student")
    print("Press 5 for Delete a Student")
    print("Press 6 for Display Unique Subjects")
    print("Press 7 for Display Student Details")
    print("Press 8 for Delete All Students")
    print("Press 0 for Exit")
    print("============================================")

    choice = int(input("Enter your choice: "))

    match choice:

        
        # 1. ADD STUDENT
      
        case 1:

            print("\n========== ADD STUDENT ==========")

            grid = int(input("Enter GR ID: "))
            name = input("Enter name: ")
            address = input("Enter Address: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            

            subjects_input = input(
                "Enter subjects (comma separated): "
            )

            # Convert input into Set
            subjects = set(
                subject.strip()
                for subject in subjects_input.split(",")
            )

            # Tuple for immutable information
            student_info = (grid, name)

            # Dictionary for student information
            student = {
                "student_info": student_info,
                "age": age,
                "grade": grade,
                "subjects": subjects,
                "address": address
            }

            students.append(student)

            print("\nStudent added successfully...")

        
        # 2. VIEW ALL STUDENTS

        case 2:

            print("\n========== ALL STUDENTS ==========")

            if not students:
                print("No students available...")

            else:
                for stu in students:

                    grid, name = stu["student_info"]

                    print(
                        f"GR ID: {grid}, "
                        f"Name: {name}, "
                        f"Address: {address}, "
                        f"Age: {stu['age']}, "
                        f"Grade: {stu['grade']}, "
                        f"Subjects: {', '.join(stu['subjects'])}"
                    )

        
        # 3. SEARCH STUDENT
       
        case 3:

            print("\n========== SEARCH STUDENT ==========")

            grid = int(input("Enter GR ID to search: "))

            found = False

            for stu in students:

                student_grid, name = stu["student_info"]

                if student_grid == grid:

                    print("\nStudent Found!")
                    print("GR ID:", student_grid)
                    print("Name:", name)
                    print("Address:", address)
                    print("Age:", stu["age"])
                    print("Grade:", stu["grade"])
                    print("Subjects:", stu["subjects"])

                    found = True
                    break

            if not found:
                print("Student not found...")

       
        # 4. UPDATE STUDENT
        
        case 4:

            print("\n========== UPDATE STUDENT ==========")

            grid = int(input("Enter GR ID to update: "))

            found = False

            for stu in students:

                student_grid, name = stu["student_info"]

                if student_grid == grid:

                    print("\n1. Update Age")
                    print("2. Update Grade")
                    print("3. Update Subjects")
                    print("4. Update address")

                    update_choice = int(
                        input("Enter your choice: ")
                    )

                    if update_choice == 1:

                        new_age = int(
                            input("Enter new age: ")
                        )

                        stu["age"] = new_age

                        print("Age updated successfully!")

                    elif update_choice == 2:

                        new_grade = input(
                            "Enter new grade: "
                        )

                        stu["grade"] = new_grade

                        print("Grade updated successfully!")

                    elif update_choice == 3:

                        new_subjects = input(
                            "Enter new subjects (comma separated): "
                        )

                        stu["subjects"] = set(
                            subject.strip()
                            for subject in new_subjects.split(",")
                        )

                        print(
                            "Subjects updated successfully!"
                        )
                    elif update_choice == 4:

                        new_address = input(
                            "Enter new address: "
                        )

                        stu["address"] = new_address

                        print("address updated successfully!")   

                    else:
                        print("Invalid choice!")

                    found = True
                    break

            if not found:
                print("Student not found...")

       
        # 5. DELETE STUDENT
        
        case 5:

            print("\n========== DELETE STUDENT ==========")

            grid = int(input("Enter GR ID to delete: "))

            found = False

            for stu in students:

                student_grid, name = stu["student_info"]

                if student_grid == grid:

                    students.remove(stu)

                    print(
                        "Student deleted successfully..."
                    )

                    found = True
                    break

            if not found:
                print("Student not found...")

        
        # 6. UNIQUE SUBJECTS
        
        case 6:

            print("\n========== UNIQUE SUBJECTS ==========")

            all_subjects = set()

            for stu in students:
                all_subjects.update(stu["subjects"])

            if all_subjects:
                print("Unique Subjects:")

                for subject in sorted(all_subjects):
                    print("-", subject)

            else:
                print("No subjects available...")

       
        # 7. STUDENT DETAILS
       
        case 7:

            print("\n========== STUDENT DETAILS ==========")

            if not students:

                print("No students available...")

            else:

                for stu in students:

                    grid, name = stu["student_info"]

                    print("\nStudent Dictionary:")
                    print(stu)

                    print("GR ID Type:", type(grid))
                    print("Name Type:", type(name))
                    print("Age Type:", type(stu["age"]))
                    print("Subjects Type:", type(stu["subjects"]))

                    print("--------------------------------")

        
        # 8. DELETE ALL STUDENTS
        
        case 8:

            print("\n========== DELETE ALL STUDENTS ==========")

            if students:

                students.clear()

                print(
                    "All students are deleted..."
                )

            else:

                print("No students available...")

        
        # 0. EXIT

        case 0:

            print("\nThank you for using Student Data Organizer!")
            print("Program Ended...")
            break

      
        # INVALID CHOICE

        case _:

            print(
                "\nInvalid choice! "
                "Please enter a valid option."
            )
