# lib/cli/main.py
import argparse
from sqlalchemy.orm import Session
from lib.models import JobApplication, User, Status, Note
from lib.database import session  # assume you create this helper

def list_applications(sort_by=None):
    query = session.query(JobApplication)
    if sort_by:
        query = query.order_by(getattr(JobApplication, sort_by))
    for app in query.all():
        print(f"{app.id} | {app.job_title} @ {app.company} | {app.status.name}")

def delete_application(app_id):
    app = session.query(JobApplication).get(app_id)
    if app:
        session.delete(app)
        session.commit()
        print(f"Deleted application with ID {app_id}")
    else:
        print("Application not found.")

def main():
    parser = argparse.ArgumentParser(description="Job Application Tracker CLI")
    subparsers = parser.add_subparsers(dest='command')

    # list
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('--sort', help="Sort by: job_title, company, applied_date")

    # delete
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('--id', type=int, required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_applications(sort_by=args.sort)
    elif args.command == 'delete':
        delete_application(args.id)

if __name__ == '__main__':
    main()
