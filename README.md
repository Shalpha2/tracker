# 📄 Job Application Tracker (CLI App)

A simple command-line tool for tracking job applications, their statuses, and personal notes per user. Ideal for developers and job seekers who want to keep an organized log of job applications locally.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 📚 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Structure](#-structure)
- [Setup Instructions](#-setup-instructions)
- [Example Usage](#-example-usage)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features

- 🔐 Register and login users
- 📝 Add new job applications
- 📋 List all applications per user
- ❌ Delete applications by ID
- 🌱 Seed sample data for testing
- Search applications by job title
- Filter applications by status (e.g., applied, rejected, interviewing)

---

## 🏗️ Tech Stack

- **Python 3.10+**
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight local database

---

## 📁 Structure

lib/
│
├── cli.py # Handles CLI interactions
├── models.py # SQLAlchemy models for User and Application
├── migrations/ # Alembic migration files
│ └── versions/
├── seed.py # Script to seed sample data
├── main.py # Entry point for the app
├── applications.db # SQLite database

yaml
Copy code

---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://https://https://github.com/Shalpha2/tracker
cd job-application-tracker-cli

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install sqlalchemy

# 5. Seed the database with initial data (optional)
python seed.py

# 6. Run the app
python main.py
🧪 Example Usage
Register a User
yaml
Copy code
Enter username: john_doe
Enter email: john@example.com
Enter password: ********
✅ Registration successful!
Log In
markdown
Copy code
Enter username: john_doe
Enter password: ********
✅ Login successful!
Add a Job Application
yaml
Copy code
Job Title: Backend Engineer
Company: Google
Status [Applied/Interview/Offer/Rejected]: Applied
Applied Date (YYYY-MM-DD): 2025-05-28
Notes: Sent follow-up email
✅ Application saved!
List Applications
markdown
Copy code
Your Applications:
--------------------------------------------------------
ID | Title            | Company | Status   | Date       |
--------------------------------------------------------
1  | Backend Engineer | Google  | Applied  | 2025-05-28 |
--------------------------------------------------------
Delete an Application
mathematica
Copy code
Enter Application ID to delete: 1
✅ Application deleted!
🔮 Future Improvements
🔐 Password hashing (e.g., using bcrypt)

📌 Persistent login session

🔍 Filter/search applications by status, company, or keyword

📤 Export applications to CSV or JSON

📅 Add reminders or follow-up dates

🧪 Unit tests for CLI functions

🤝 Contributing
Contributions are welcome and encouraged! Please follow these steps:

Fork the repo

Create a new branch: git checkout -b feature/your-feature-name

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin feature/your-feature-name

Open a pull request

Feel free to open an issue if you find bugs or have feature requests!

🐛 Known Issues
Passwords are stored in plain text (⚠️ security risk)

No email validation during registration

Cannot edit or update existing applications

No input validation for dates or status values

📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Thanks to SQLAlchemy for making ORM easy in Python.

Inspired by the need to manage job applications effectively during job hunting.