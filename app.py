from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students")
def get_students():
    students = [
        {"name": "John Doe", "program": "Software Engineering"},
        {"name": "Jane Smith", "program": "Computer Science"},
        {"name": "Ali Musa", "program": "Information Technology"},
        {"name": "Emily Chen", "program": "Software Engineering"},
        {"name": "Carlos Ruiz", "program": "Computer Engineering"},
        {"name": "Fatima Noor", "program": "Software Engineering"},
        {"name": "Daniel Kim", "program": "Information Systems"},
        {"name": "Grace Lee", "program": "Software Engineering"},
        {"name": "Ahmed Khan", "program": "Cyber Security"},
        {"name": "Maryam Bello", "program": "Software Engineering"}
    ]
    return jsonify(students)

@app.route("/subjects")
def get_subjects():
    subjects = {
        "Year 1": ["Introduction to Programming", "Calculus I", "Digital Logic", "Communication Skills"],
        "Year 2": ["Data Structures", "Database Systems", "Operating Systems", "Web Technologies"],
        "Year 3": ["Software Engineering", "Artificial Intelligence", "Mobile App Development", "Computer Networks"],
        "Year 4": ["Project Management", "Cloud Computing", "Machine Learning", "Final Year Project"]
    }
    return jsonify(subjects)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



