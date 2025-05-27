import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import User, Status, JobApplication

# Setup DB connection
engine = create_engine('sqlite:///applications.db')
Session = sessionmaker(bind=engine)
session = Session()

def register_user():
    print("\n📝 Register")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    user = User(username=username, email=email, password_hash=password)
    session.add(user)
    session.commit()
    print("✅ User registered.")

def login_user():
    print("\n🔐 Login")
    username = input("Username: ")
    password = input("Password: ")
    user = session.query(User).filter_by(username=username, password_hash=password).first()
    return user

def list_applications():
    applications = session.query(JobApplication).all()
    if applications:
        for app in applications:
            print(f"\nID: {app.id}")
            print(f"Title: {app.job_title}")
            print(f"Company: {app.company}")
            print(f"Status: {app.status.name}")
            print(f"Applied Date: {app.applied_date}")
            print(f"User: {app.user.username}")
            print(f"Note: {app.note}")
    else:
        print("No applications found.")

def add_application():
    username = input("Username: ")
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print(f"No user found with username: {username}")
        return

    job_title = input("Job Title: ")
    company = input("Company: ")
    status_name = input("Status (Applied/Interview/Offer): ")
    status = session.query(Status).filter_by(name=status_name).first()
    if not status:
        print(f"Invalid status: {status_name}")
        return

    date_str = input("Applied Date (YYYY-MM-DD): ")
    note = input("Note: ")

    try:
        new_app = JobApplication(
            job_title=job_title,
            company=company,
            status=status,
            applied_date=date_str,
            note=note,
            user=user
        )
        session.add(new_app)
        session.commit()
        print("✅ Job application added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def delete_application():
    app_id = input("Enter the ID of the application to delete: ")
    app = session.query(JobApplication).filter_by(id=app_id).first()
    if app:
        session.delete(app)
        session.commit()
        print("🗑️ Application deleted.")
    else:
        print("❌ Application not found.")

def help_menu():
    print("\nAvailable commands:")
    print("  register      - Register a new user")
    print("  login         - Log in as a user")
    print("  list          - List all job applications")
    print("  add           - Add a new job application")
    print("  delete        - Delete a job application by ID")
    print("  help          - Show this help menu")
    print("  exit          - Exit the program\n")

def main():
    while True:
        print("\n📋 Choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. List Applications")
        print("4. Add Application")
        print("5. Delete Application")
        print("6. Help")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            list_applications()
        elif choice == "4":
            add_application()
        elif choice == "5":
            delete_application()
        elif choice == "6":
            help_menu()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 7.")

