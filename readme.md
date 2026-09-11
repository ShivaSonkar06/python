# 🎓 Student Data Organizer


### 📚 Simple • Creative • Beginner Friendly • Python Project 🐍

A **command-line Student Management System** built with Python to add, view, search, update and delete student records.

</div>

---

## 🌟 Project Overview

**Student Data Organizer** is a simple Python project designed to make student-record management easy through an interactive menu.

The application allows users to perform different operations such as **adding students, viewing records, searching by GR ID, updating information, deleting records, and finding unique subjects**. The program uses Python's built-in data structures to organize the information.

---

## ✨ Features

| Option | Feature | Description |
|:---:|---|---|
| 1️⃣ | ➕ Add Student | Add a new student with GR ID, name, address, age, grade and subjects |
| 2️⃣ | 👀 View All Students | Display all currently stored students |
| 3️⃣ | 🔍 Search Student | Find a student using GR ID |
| 4️⃣ | ✏️ Update Student | Update age, grade, subjects or address |
| 5️⃣ | 🗑️ Delete Student | Delete a selected student |
| 6️⃣ | 📚 Unique Subjects | Display all unique subjects |
| 7️⃣ | 📋 Student Details | Display student dictionary and data types |
| 8️⃣ | 🧹 Delete All | Remove all student records |
| 0️⃣ | 🚪 Exit | Close the application |

The menu and these operations are implemented in the uploaded Python project. 

---

## 🧠 Python Concepts Used

This project is especially useful for understanding Python **data types and data structures**.

### 📦 List
Used to store multiple student records.

```python
students = []
```

### 📖 Dictionary
Each student is represented using a dictionary containing student information, age, grade, subjects and address.

### 🔒 Tuple
GR ID and name are stored together as a tuple.

```python
student_info = (grid, name)
```

### 🎯 Set
Subjects are stored as a set, which automatically helps avoid duplicate subjects.

```python
subjects = set(...)
```

### 🔁 While Loop
Keeps the application menu running until the user chooses Exit.

### 🔀 Match-Case
Used to handle the different menu options.

---

## 🖥️ Application Menu

```text
========== STUDENT DATA ORGANIZER ==========

Press 1 for Add a Student
Press 2 for View All Students
Press 3 for Search a Student
Press 4 for Update a Student
Press 5 for Delete a Student
Press 6 for Display Unique Subjects
Press 7 for Display Student Details
Press 8 for Delete All Students
Press 0 for Exit

============================================
```

---

## 📸 Screenshots
<img width="798" height="927" alt="Screenshot 2026-09-11 124207" src="https://github.com/user-attachments/assets/4b09a0b9-d260-450f-aab8-d3787b9f4a4f" />

<img width="911" height="927" alt="Screenshot 2026-09-11 124050" src="https://github.com/user-attachments/assets/4d7cec63-2836-49a2-b079-bb56cee09584" />
<img width="935" height="938" alt="Screenshot 2026-09-11 124131" src="https://github.com/user-attachments/assets/1868ced0-898a-4160-b604-33fc94204165" />
<img width="772" height="872" alt="Screenshot 2026-09-11 124012" src="https://github.com/user-attachments/assets/f21846bf-da01-4de1-9225-a5e4adaab661" />


---

### 👀 Viewing & 🔍 Searching Students

Multiple student records can be displayed, and a student can be searched using their GR ID.

![View and Search](screenshots/view-and-search.png)

---

### 🗑️ Deleting & 🚪 Exiting

The system provides options for deleting all records and safely exiting the program.

![Delete and Exit](screenshots/delete-and-exit.png)

---

### 🧹 Delete All & 📋 Student Details

The application can clear all stored students and display detailed information about the stored data.

![Delete All and Details](screenshots/delete-all-and-details.png)

---

## 🚀 How to Run

### 1️⃣ Install Python

Make sure Python 3 is installed on your computer.

Check it using:

```bash
python --version
```

### 2️⃣ Download / Clone the Project

Place the Python file in your desired folder.

### 3️⃣ Open Terminal

Open Command Prompt or Terminal inside the project folder.

### 4️⃣ Run the Program

```bash
python "Student_management_system(2).py"
```

### 5️⃣ Start Using the Menu 🎉

Enter a number from **0 to 8** and follow the instructions shown on the screen.

---

## 📝 Example

### 👤 Add Student

```text
Enter GR ID: 12465
Enter name: shiva sonkar
Enter Address: navsari
Enter age: 22
Enter grade: A+
Enter subjects (comma separated): AI/ML,GRAPHIC DESIGN

Student added successfully...
```

### 👥 View Students

```text
GR ID: 12465, Name: shiva sonkar, Age: 22,
Grade: A+, Subjects: GRAPHIC DESIGN, AI/ML
```

---

## 🔄 CRUD Operations

This project demonstrates the basic **CRUD** concept:

- 🟢 **Create** → Add Student
- 🔵 **Read** → View / Search Student
- 🟡 **Update** → Update Student
- 🔴 **Delete** → Delete Student / Delete All

---

## 📂 Suggested Project Structure

```text
Student-Management-System/
│
├── Student_management_system(2).py
├── README.md
│
└── screenshots/
    ├── add-students.png
    ├── view-and-search.png
    ├── delete-and-exit.png
    └── delete-all-and-details.png
```

---
demo video


https://github.com/user-attachments/assets/d3ada2b2-660e-4eb6-abec-8f59cd450854





## ⚡ Important Note

This version stores student records **temporarily in memory** while the program is running.

If the program is closed, the stored records are not automatically saved to a permanent database or file.

---

## 🔮 Future Improvements

Some ideas to make the project even more dynamic:

- 💾 Add permanent database storage
- 🎨 Create a graphical user interface
- 🔐 Add login / authentication
- 📊 Add student performance reports
- 📈 Add marks and percentage calculation
- 📤 Export student data to CSV or Excel
- 🔎 Add advanced search and filters
- ✅ Add stronger input validation

---

## 🎯 Learning Goals

By completing this project, you can practice:

```text
🐍 Python Basics
📦 Lists
📖 Dictionaries
🔒 Tuples
🎯 Sets
🔁 Loops
🔀 Match-Case
🧠 Conditional Logic
📝 User Input
🔄 CRUD Operations
```

---

## ❤️ Why This Project?

> 🎓 A simple project with practical use  
> 🐍 Great for learning Python data structures  
> 💡 Easy to understand and customize  
> 🚀 Perfect for a beginner-level GitHub project  

---

## 👨‍💻 Author

### **Shiva Sonkar** 🚀

Made with ❤️ and Python 🐍

---

<div align="center">

### ⭐ If you like this project, give it a star on GitHub!

**Happy Coding! 💻🔥**

</div>
