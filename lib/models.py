from sqlalchemy import ForeignKey, Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base, relationship
import re    #regex for validation
from sqlalchemy.orm import validates
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True)
    username = Column(String,unique=True , nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    job_applications = relationship('JobApplication', back_populates='user')

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email})>'  
    
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError(" Invalid email format")
        
        return email

    @validates('password_hash')
    def validate_password(self, key, password):
        if len(password) < 8:
            raise ValueError(" Password must be at least 8 characters long")
       
        return password

class Status(Base):
    __tablename__ = 'status'  

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    job_applications = relationship('JobApplication', back_populates='status')

    def __repr__(self):
        return f'<Status(name={self.name})>'


class JobApplication(Base):
    __tablename__ = 'job_application'  

    id = Column(Integer, primary_key=True)
    job_title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey('status.id'))
    applied_date = Column(Date)
    note = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='job_applications')
    status = relationship('Status', back_populates='job_applications')

    def __repr__(self):
        return f'<JobApplication(job_title={self.job_title}, company={self.company})>'  







