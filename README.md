# 🏥 Patient Triage System

A web-based **Patient Triage System** developed using **Python Flask and SQLite**. The system allows hospital staff to register patients, automatically assign a triage priority based on reported symptoms, and manage the patient queue through a dashboard.

> **Note:** This is an academic/software demonstration project. The symptom-priority rules are based on the application's programmed keyword logic and are **not a medically validated clinical decision-making system**.

---

## 📌 Project Overview

The Patient Triage System is designed to help organize patients according to the urgency of their symptoms.

The system provides:

* Patient registration
* Patient ID generation
* Symptom selection
* Automatic priority calculation
* Critical, Moderate, and Low priority classification
* Patient queue management
* Waiting-time estimation
* Patient deletion
* Dashboard for monitoring registered patients
* SQLite database storage

The original application uses Flask and connects to a SQLite database named `hospital.db`. The database contains a `patients` table with patient ID, name, age, symptoms, priority, and waiting-time fields.

---

## 🛠️ Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Backend programming                |
| Flask      | Web application framework          |
| SQLite     | Database                           |
| HTML       | Frontend structure                 |
| CSS        | Frontend styling                   |
| Jinja2     | Dynamic HTML rendering             |
| PowerShell | Running the application on Windows |

---

## 📂 Project Structure

```text
patient-triage-original-style/
│
├── app.py
│
├── hospital.db
│
├── requirements.txt
│
├── Procfile
│
├── runtime.txt
│
├── README.md
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

### File Description

#### `app.py`

Main Flask application containing:

* Database connection
* Database initialization
* Patient registration
* Patient ID generation
* Priority calculation
* Patient deletion
* Dashboard
* Waiting-time calculation

#### `hospital.db`

SQLite database containing patient information.

#### `templates/index.html`

Patient registration page.

#### `templates/dashboard.html`

Patient triage dashboard.

#### `static/style.css`

Styling for the web application.

#### `requirements.txt`

Contains the Python dependency required to run the application.

#### `Procfile`

Used for deployment platforms such as Render.

#### `runtime.txt`

Specifies the Python runtime version for deployment.

---

# ⚙️ Installation

## 1. Install Python

Make sure Python is installed on your computer.

Check:

```powershell
py --version
```

or:

```powershell
python --version
```

If Python is installed correctly, you should see a version such as:

```text
Python 3.11.x
```

---

# 📥 2. Open the Project

Extract the project ZIP.

Open the project folder in **VS Code**.

The terminal should be inside:

```text
patient-triage-original-style
```

For example:

```text
C:\Users\DELL\Downloads\patient-triage-original-style
```

---

# 🐍 3. Create a Virtual Environment

Run:

```powershell
py -m venv venv
```

This creates:

```text
venv/
```

inside the project.

---

# 🔌 4. Activate the Virtual Environment

If PowerShell allows script execution:

```powershell
venv\Scripts\activate
```

If PowerShell blocks the activation script, use:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
venv\Scripts\activate
```

You should see:

```text
(venv) PS C:\Users\DELL\Downloads\patient-triage-original-style>
```

---

# 📦 5. Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

The project currently requires Flask.

---

# ▶️ 6. Run the Application

Run:

```powershell
python app.py
```

You should see:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

---

# 🌐 7. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

You should see the **Patient Triage System**.

---

# 📝 Patient Registration

From the home page, enter:

* Patient Name
* Age
* Symptoms

Then click:

**Register Patient**

The application sends the patient information to the Flask backend.

The backend calculates the priority and stores the patient in `hospital.db`.

The original application inserts the patient into the `patients` table with:

```text
id
name
age
symptoms
priority
waiting_time
```

---

# 🚨 Triage Priority System

The application uses symptom keywords to determine priority.

## 🔴 Priority 3 — Critical

The original application checks for keywords such as:

```text
chest
breathing
unconscious
stroke
suicide
poison
self harm
pregnancy bleeding
accident
```

If a critical keyword is found, the patient receives:

```text
Priority = 3
```

The original priority function implements these critical keywords directly.

---

## 🟠 Priority 2 — Moderate

The application checks for:

```text
fever
abdominal pain
fracture
```

These result in:

```text
Priority = 2
```

---

## 🟢 Priority 1 — Low

The application checks for:

```text
headache
cold
body pain
```

These result in:

```text
Priority = 1
```

If none of the defined keywords match, the original application defaults to:

```text
Priority = 1
```

---

# 📊 Dashboard

The dashboard displays registered patients according to their priority.

Patients are ordered using:

```text
Priority DESC
ID ASC
```

Therefore, higher-priority patients appear before lower-priority patients.

The original dashboard also calculates estimated waiting time based on the patients ahead in the queue.

---

# ⏱️ Waiting Time

The application uses the following consultation-time assumptions:

| Priority | Category | Consultation Time |
| -------: | -------- | ----------------: |
|        3 | Critical |         5 minutes |
|        2 | Moderate |        10 minutes |
|        1 | Low      |        15 minutes |

The waiting time for each patient is calculated from the consultation times of patients appearing before them in the queue.

These values come directly from the application's programmed dashboard logic.

---

# 🗑️ Delete Patient

The dashboard provides a delete option for each patient.

The application uses:

```text
/delete/<patient_id>
```

to remove the selected patient from the database.

---

# 🗄️ Database

The application uses SQLite.

Database:

```text
hospital.db
```

Table:

```text
patients
```

Structure:

```text
id
name
age
symptoms
priority
waiting_time
```

The Flask application automatically creates the `patients` table if it does not already exist.

---

# 🔢 Patient ID

The application contains custom logic for finding the smallest available patient ID.

For example, if the database contains:

```text
1
2
3
5
6
```

the next patient receives:

```text
4
```

instead of automatically using `7`.

---

# 🔧 Troubleshooting

## Python is not recognized

If you see:

```text
python : The term 'python' is not recognized
```

try:

```powershell
py --version
```

If that works, use:

```powershell
py -m venv venv
```

and:

```powershell
py app.py
```

---

## PowerShell blocks activation

If you see:

```text
running scripts is disabled on this system
```

run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
venv\Scripts\activate
```

---

## Flask is not installed

Run:

```powershell
pip install -r requirements.txt
```

---

## Port 5000 is already in use

Stop the existing Flask application with:

```text
CTRL + C
```

Then run:

```powershell
python app.py
```

If necessary, the Flask port can be changed in `app.py`.

---

## Database problems

Make sure:

```text
hospital.db
```

is in the same directory as:

```text
app.py
```

The application connects using:

```text
hospital.db
```

---

# ☁️ Deployment

The project also contains:

```text
Procfile
runtime.txt
requirements.txt
```

for deployment.

The Procfile uses:

```text
gunicorn app:app
```

For a Render deployment, the project can be connected to a GitHub repository and deployed as a Python web service.

---

# 🔄 Application Flow

```text
User
  ↓
Patient Registration Page
  ↓
Enter Patient Details
  ↓
Select Symptoms
  ↓
Flask Backend
  ↓
Priority Calculation
  ↓
Store Patient in SQLite
  ↓
Dashboard
  ↓
Priority-Based Patient Queue
  ↓
Estimated Waiting Time
```

---

# 🎯 Project Objectives

The main objectives of the Patient Triage System are:

1. To digitally register patients.
2. To organize patients based on symptom priority.
3. To reduce manual patient queue management.
4. To automatically calculate priority.
5. To estimate patient waiting time.
6. To provide a simple dashboard for hospital staff.
7. To store patient information using SQLite.

---

# ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.

The triage rules are simple keyword-based software logic and have not been clinically validated.

The system must **not** be used to diagnose patients, determine actual medical emergencies, replace healthcare professionals, or make real-world treatment decisions.

For real healthcare deployment, the system would require appropriate clinical validation, security, privacy protection, authentication, auditing, monitoring, and regulatory review.

---

# 👨‍💻 Project

**Patient Triage System**

**Technology:** Python + Flask + SQLite + HTML + CSS

**Application Type:** Healthcare Management / Triage Demonstration System
