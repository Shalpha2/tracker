from sqlalchemy import ForeignKey, Column, Integer, String, Text, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    job_applications = relationship('JobApplication', back_populates='user')

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email})>'  


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







