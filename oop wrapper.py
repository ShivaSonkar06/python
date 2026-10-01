print("---python oop project : employee management system---")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Person: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Age: {self.age}, ID: {self.employee_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_details(self):
        print(f"Manager: {self.name}, Age: {self.age}, ID: {self.employee_id}, Salary: {self.salary}, Department: {self.department}")


people = []

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        people.append(person)

        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == "2":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, employee_id, salary)
        people.append(employee)

        print(f"\nEmployee created with name: {name}.")

    elif choice == "3":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, employee_id, salary, department)
        people.append(manager)

        print(f"\nManager created with name: {name}.")

    elif choice == "4":
        print("\n--- Details ---")

        if len(people) == 0:
            print("No details available.")
        else:
            for person in people:
                person.show_details()

    elif choice == "5":
        print("\nThank you for using Employee Management System.")
        break

    else:
        print("\nInvalid choice.")

    if choice != "5":
        print("\n--- Choose another operation ---")
       
