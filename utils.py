import pandas as pd
from fpdf import FPDF
from pathlib import Path

def save_csv_excel(data):
    record = {
        "Name": data["name"],
        "Roll No": data["roll"],
        "Subject 1": data["marks"][0],
        "Subject 2": data["marks"][1],
        "Subject 3": data["marks"][2],
        "Subject 4": data["marks"][3],
        "Subject 5": data["marks"][4],
        "Total": data["total"],
        "Average": data["average"],
        "Percentage": data["percentage"],
        "Grade": data["grade"],
        "Status": data["status"]
    }

    file = Path("student_records.csv")

    if file.exists():
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    else:
        df = pd.DataFrame([record])

    df.to_csv("student_records.csv", index=False)
    df.to_excel("student_records.xlsx", index=False)

def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, "Student Report Card", ln=True, align="C")

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)

    pdf.cell(200, 10, f"Name: {data['name']}", ln=True)
    pdf.cell(200, 10, f"Roll No: {data['roll']}", ln=True)

    for i, mark in enumerate(data["marks"], start=1):
        pdf.cell(200, 10, f"Subject {i}: {mark}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, f"Total Marks: {data['total']}", ln=True)
    pdf.cell(200, 10, f"Average: {data['average']}", ln=True)
    pdf.cell(200, 10, f"Percentage: {data['percentage']}%", ln=True)
    pdf.cell(200, 10, f"Grade: {data['grade']}", ln=True)
    pdf.cell(200, 10, f"Result: {data['status']}", ln=True)

    pdf.output("report_card.pdf")
