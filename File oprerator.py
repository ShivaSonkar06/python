print("Welcome to Personal Journal Manager!")
print("Please select an option:")

while True:
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nUser Input: ")

    if choice == "1":
        entry = input("\nEnter your journal entry: ")

        with open("journal.txt", "a") as file:
            file.write(entry + "\n")

        print("\nEntry added successfully!")

    elif choice == "2":
        with open("journal.txt", "r") as file:
            entries = file.read()

        print("\nAll Journal Entries:")
        print(entries)

    elif choice == "3":
        search = input("\nEnter word to search: ")

        with open("journal.txt", "r") as file:
            entries = file.readlines()

        for entry in entries:
            if search.lower() in entry.lower():
                print(entry)

    elif choice == "4":
        with open("journal.txt", "w") as file:
            file.write("")

        print("\nAll entries deleted successfully!")

    elif choice == "5":
        print("\n Thnks for using Personal Journal Manager.Goodbye!")
        break

    else:
        print("\nInvalid option!")
