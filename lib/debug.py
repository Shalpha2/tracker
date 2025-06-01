# debug.py
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import User, Status, JobApplication
from datetime import datetime, date
import ipdb
# Setup DB connection
#engine = create_engine('sqlite:///applications.db')
#Session = sessionmaker(bind=engine)
#session = Session()



#  Test invalid email
#try:
   # print(" Testing invalid email format...")
   # bad_user = User(username="BadEmailUser", email="notanemail", password_hash="12345678")
  #  session.add(bad_user)
    #session.commit()
#except Exception as e:
  #  print(f" Caught error as expected: {e}")
  #  session.rollback()

#  Test short password
#try:
    #print("\n Testing short password...")
    ##short_pass_user = User(username="ShortPass", email="short@pass.com", password_hash="123")
   ## session.add(short_pass_user)
 #   session.commit()
#except Exception as e:
  #  print(f" Caught error as expected: {e}")
  #  session.rollback()

#  Test login with wrong credentials
#print("\n Testing login with wrong credentials...")
#username = "Ezekiel"
#wrong_password = "wrongpassword"
#user = session.query(User).filter_by(username=username, password_hash=wrong_password).first()
#if not user:
    #print(" Login failed as expected for wrong password.")



#  Test retrieving and printing all current users
#print("\n Current Users:")
#for u in session.query(User).all():
  #  print(f" - {u.username} | {u.email}")

# Test printing all current job applications
#print("\nCurrent Job Applications:")
#for app in session.query(JobApplication).all():
   # print(f" - {app.job_title} at {app.company} | Status: {app.status.name}")

#ipdb.set_trace()
