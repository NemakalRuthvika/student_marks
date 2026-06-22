from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

def save_csv_excel(result):
    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Roll", "Total", "Average", "Percentage", "Grade", "Status"])

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
    # PDF code can be added later
    pass

def insert_student(result):
    # Database code can be added later
    pass

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    try:
        if request.method == "POST":
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
            average = total / 5
            percentage = (total / 500) * 100

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

            status = "PASS" if all(mark >= 35 for mark in marks) else "FAIL"

            result = {
                "name": name,
                "roll": roll,
                "marks": marks,
                "total": total,
                "average": average,
                "percentage": round(percentage, 2),
                "grade": grade,
                "status": status
            }

            save_csv_excel(result)
            generate_pdf(result)
            insert_student(result)

    except Exception as e:
        return f"ERROR: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)