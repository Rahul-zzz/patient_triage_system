# Patient Triage System — Original-Style Rebuild

This project was rebuilt from the uploaded `app(1).py` and `hospital.db`.

## Technology

- Flask
- SQLite
- HTML/CSS
- Jinja templates

## Structure

```text
patient-triage-original-style/
├── app.py
├── hospital.db
├── requirements.txt
├── Procfile
├── runtime.txt
├── templates/
│   ├── index.html
│   └── dashboard.html
└── static/
    └── style.css
```

## Run locally

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open:

http://127.0.0.1:5000

## What is preserved from the uploaded application

- `hospital.db` is the uploaded database.
- Patient table fields: id, name, age, symptoms, priority, waiting_time.
- Smallest missing patient ID logic.
- Symptom keyword priority logic.
- `/`, `/add_patient`, `/delete/<id>`, and `/dashboard` routes.
- Dashboard priority ordering.
- Waiting-time calculation:
  - Priority 3: 5 minutes
  - Priority 2: 10 minutes
  - Priority 1: 15 minutes

The only source-code correction made to the uploaded Python file was the malformed final `__name__` guard so the application can execute.

## Important

The recreated HTML/CSS is an original reconstruction because those frontend files were not included in the uploaded source. It follows the functionality exposed by the uploaded Flask application.

The symptom keyword rules are software rules from the uploaded project, not medically validated clinical guidance.
