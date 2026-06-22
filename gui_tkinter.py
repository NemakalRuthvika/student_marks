import tkinter as tk
from tkinter import messagebox
from utils import save_csv_excel, generate_pdf
from db import insert_student

def calculate():
    try:
        name = name_entry.get()
        roll = roll_entry.get()

        marks = [
            float(sub1_entry.get()),
            float(sub2_entry.get()),
            float(sub3_entry.get()),
            float(sub4_entry.get()),
            float(sub5_entry.get())
        ]

        total = sum(marks)
        average = total / 5
        percentage = (total / 500) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 35:
            grade = "D"
        else:
            grade = "F"

        status = "PASS" if percentage >= 35 else "FAIL"

        data = {
            "name": name,
            "roll": roll,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": round(percentage, 2),
            "grade": grade,
            "status": status
        }

        save_csv_excel(data)
        generate_pdf(data)

        try:
            insert_student(data)
        except Exception as e:
            print("MySQL Error:", e)

        result_label.config(
            text=f"Total: {total}\nAverage: {average}\nPercentage: {round(percentage,2)}%\nGrade: {grade}\nResult: {status}"
        )

        messagebox.showinfo("Success", "Record saved, Excel/CSV updated, PDF generated!")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid marks.")

root = tk.Tk()
root.title("Student Marks Calculator")
root.geometry("400x500")

tk.Label(root, text="Student Marks Calculator", font=("Arial", 16, "bold")).pack(pady=10)

name_entry = tk.Entry(root)
roll_entry = tk.Entry(root)
sub1_entry = tk.Entry(root)
sub2_entry = tk.Entry(root)
sub3_entry = tk.Entry(root)
sub4_entry = tk.Entry(root)
sub5_entry = tk.Entry(root)

fields = [
    ("Name", name_entry),
    ("Roll No", roll_entry),
    ("Subject 1", sub1_entry),
    ("Subject 2", sub2_entry),
    ("Subject 3", sub3_entry),
    ("Subject 4", sub4_entry),
    ("Subject 5", sub5_entry),
]

for label, entry in fields:
    tk.Label(root, text=label).pack()
    entry.pack(pady=3)

tk.Button(root, text="Calculate & Save", command=calculate).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
