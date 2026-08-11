from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect("hospital.db")
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# INITIALIZE DATABASE
# -----------------------------
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            symptoms TEXT,
            priority INTEGER,
            waiting_time INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# FIND SMALLEST MISSING ID
# -----------------------------
def get_next_available_id():
    conn = get_db_connection()
    ids = conn.execute("SELECT id FROM patients ORDER BY id").fetchall()
    conn.close()

    existing_ids = [row["id"] for row in ids]

    next_id = 1
    for id_val in existing_ids:
        if id_val != next_id:
            return next_id
        next_id += 1

    return next_id

# -----------------------------
# PRIORITY CALCULATION
# -----------------------------
def calculate_priority(symptoms):
    symptoms = symptoms.lower()

    critical_keywords = [
        "chest", "breathing", "unconscious", "stroke",
        "suicide", "poison", "self harm",
        "pregnancy bleeding", "accident"
    ]

    moderate_keywords = ["fever", "abdominal pain", "fracture"]
    low_keywords = ["headache", "cold", "body pain"]

    for word in critical_keywords:
        if word in symptoms:
            return 3

    for word in moderate_keywords:
        if word in symptoms:
            return 2

    for word in low_keywords:
        if word in symptoms:
            return 1

    return 1

# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -----------------------------
# ADD PATIENT
# -----------------------------
@app.route("/add_patient", methods=["POST"])
def add_patient():
    name = request.form["name"]
    age = request.form["age"]
    symptoms = request.form["symptoms"]
    other_symptom = request.form.get("other_symptom")

    if symptoms.lower() == "other" and other_symptom:
        symptoms = other_symptom

    priority = calculate_priority(symptoms)
    new_id = get_next_available_id()

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO patients (id, name, age, symptoms, priority, waiting_time) VALUES (?, ?, ?, ?, ?, ?)",
        (new_id, name, age, symptoms, priority, 0),
    )
    conn.commit()
    conn.close()

    return redirect("/dashboard")

# -----------------------------
# DELETE PATIENT
# -----------------------------
@app.route("/delete/<int:id>")
def delete_patient(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM patients WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/dashboard")

# -----------------------------
# DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():
    conn = get_db_connection()
    patients = conn.execute(
        "SELECT * FROM patients ORDER BY priority DESC, id ASC"
    ).fetchall()

    updated_patients = []
    waiting_time = 0

    critical_count = 0
    moderate_count = 0
    low_count = 0

    for patient in patients:
        updated_patient = list(patient)

        if updated_patient[4] == 3:
            consultation_time = 5
            critical_count += 1
        elif updated_patient[4] == 2:
            consultation_time = 10
            moderate_count += 1
        else:
            consultation_time = 15
            low_count += 1

        updated_patient[5] = waiting_time
        waiting_time += consultation_time

        updated_patients.append(updated_patient)

    conn.close()

    return render_template(
        "dashboard.html",
        patients=updated_patients,
        critical_count=critical_count,
        moderate_count=moderate_count,
        low_count=low_count,
    )

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)