from flask import Flask, render_template, request, send_file
import csv
import os
from reportlab.pdfgen import canvas

app = Flask(__name__)

def save_csv_excel(result):
    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name", "Roll", "Total",
                "Average", "Percentage",
                "Grade", "Status"
            ])

        writer.writerow([
            result["name"],
            result["roll"],
            result["total"],
            result["average"],
            result["percentage"],
            result["grade"],
            result["status"]
        ])

def generate_pdf(result):
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{result['roll']}_Report.pdf"

    pdf = canvas.Canvas(filename)

    pdf.setTitle("Student Result Report")

    pdf.drawString(100, 800, "STUDENT RESULT REPORT")
    pdf.drawString(100, 770, f"Name: {result['name']}")
    pdf.drawString(100, 750, f"Roll No: {result['roll']}")

    pdf.drawString(100, 720, f"Subject 1: {result['marks'][0]}")
    pdf.drawString(100, 700, f"Subject 2: {result['marks'][1]}")
    pdf.drawString(100, 680, f"Subject 3: {result['marks'][2]}")
    pdf.drawString(100, 660, f"Subject 4: {result['marks'][3]}")
    pdf.drawString(100, 640, f"Subject 5: {result['marks'][4]}")

    pdf.drawString(100, 600, f"Total: {result['total']}")
    pdf.drawString(100, 580, f"Average: {result['average']}")
    pdf.drawString(100, 560, f"Percentage: {result['percentage']}%")
    pdf.drawString(100, 540, f"Grade: {result['grade']}")
    pdf.drawString(100, 520, f"Status: {result['status']}")

    pdf.save()

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        try:
            name = request.form["name"]
            roll = request.form["roll"]

            marks = [
                float(request.form["sub1"]),
                float(request.form["sub2"]),
                float(request.form["sub3"]),
                float(request.form["sub4"]),
                float(request.form["sub5"])
            ]

            total = sum(marks)
            average = round(total / 5, 2)
            percentage = round((total / 500) * 100, 2)

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 75:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 40:
                grade = "C"
            else:
                grade = "F"

            status = "PASS" if all(m >= 35 for m in marks) else "FAIL"

            result = {
                "name": name,
                "roll": roll,
                "marks": marks,
                "total": total,
                "average": average,
                "percentage": percentage,
                "grade": grade,
                "status": status
            }

            save_csv_excel(result)
            generate_pdf(result)

        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html", result=result)

@app.route("/download/<roll>")
def download_pdf(roll):
    return send_file(
        f"reports/{roll}_Report.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)