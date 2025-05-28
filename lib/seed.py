from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Status, JobApplication

# Create engine and session
engine = create_engine('sqlite:///applications.db')  
Session = sessionmaker(bind=engine)
session = Session()

#Clear all tables and recreate them
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session.query(JobApplication).delete()
session.query(Status).delete()
session.query(User).delete()


# Create users
user1 = User(username="Ezekiel", email="ezekiel@gmail.com",  password_hash='defaultpasswordhash')
user2 = User(username="Abigail", email="abigail@gmail.com",  password_hash='defaultpasswordhash')

# Create statuses
status_applied = Status(name="Applied")
status_interview = Status(name="Interview")
status_offer = Status(name="Offer")

# Create job applications
job1 = JobApplication(
    job_title="Backend Developer",
    company="TechCorp",
    status=status_applied,
    applied_date=date(2025, 5, 1),
    note="Followed up via email. Waiting for response.",
    user=user1
)

job2 = JobApplication(
    job_title="Frontend Developer",
    company="Designify",
    status=status_interview,
    applied_date=date(2025, 5, 5),
    note="Scheduled interview for next week.",
    user=user2
)


session.add_all([
    user1, user2,
    status_applied, status_interview, status_offer,
    job1, job2
])
session.commit()

print("🌱 Seed data added successfully!")

