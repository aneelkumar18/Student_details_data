import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to add student details to the database
def add_student(name, age, roll_no, course):
    conn = sqlite3.connect('student_db.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, roll_no, course) VALUES (?, ?, ?, ?)", (name, age, roll_no, course))
    conn.commit()
    conn.close()

# Function to fetch and display all students from the database
def view_students():
    conn = sqlite3.connect('student_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students

# GUI class for the student form
class StudentForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details Form")

        # Name Label and Entry
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        # Age Label and Entry
        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1)

        # Roll Number Label and Entry
        self.roll_no_label = tk.Label(root, text="Roll Number:")
        self.roll_no_label.grid(row=2, column=0)
        self.roll_no_entry = tk.Entry(root)
        self.roll_no_entry.grid(row=2, column=1)

        # Course Label and Entry
        self.course_label = tk.Label(root, text="Course:")
        self.course_label.grid(row=3, column=0)
        self.course_entry = tk.Entry(root)
        self.course_entry.grid(row=3, column=1)

        # Add Student Button
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=4, column=0, columnspan=2)

        # View Students Button
        self.view_button = tk.Button(root, text="View Students", command=self.view_students)
        self.view_button.grid(row=5, column=0, columnspan=2)

        # Listbox to display students
        self.students_listbox = tk.Listbox(root, height=10, width=50)
        self.students_listbox.grid(row=6, column=0, columnspan=2)

    def add_student(self):
        # Get data from the input fields
        name = self.name_entry.get()
        age = self.age_entry.get()
        roll_no = self.roll_no_entry.get()
        course = self.course_entry.get()

        if name and age.isdigit() and roll_no and course:
            # Call the function to add student details to the database
            add_student(name, int(age), roll_no, course)
            messagebox.showinfo("Success", f"Student {name} added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields with valid data.")

    def view_students(self):
        # Clear the current list in the listbox
        self.students_listbox.delete(0, tk.END)

        # Fetch students from the database
        students = view_students()
        
        # Insert each student record into the listbox
        for student in students:
            self.students_listbox.insert(tk.END, f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Roll No: {student[3]} | Course: {student[4]}")

# Main function to run the application
if __name__ == "__main__":
    # Create the database and table if not exists
    conn = sqlite3.connect('student_db.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        roll_no TEXT NOT NULL,
                        course TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

    # Create Tkinter window
    root = tk.Tk()

    # Initialize the StudentForm class
    app = StudentForm(root)

    # Run the Tkinter event loop
    root.mainloop()
