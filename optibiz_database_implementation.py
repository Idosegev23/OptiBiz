import sqlalchemy as db
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)


class Organization(Base):
    __tablename__ = 'organizations'
    organization_id = Column(Integer, primary_key=True)
    organization_name = Column(String)
    address = Column(String)
    phone = Column(String)


class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String)
    organization_id = Column(Integer, ForeignKey('organizations.organization_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)

    organization = relationship('Organization', back_populates='projects')


class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_description = Column(String)
    quantity = Column(Integer)
    organization_id = Column(Integer, ForeignKey('organizations.organization_id'))

    organization = relationship('Organization', back_populates='inventory')


class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)

    project = relationship('Project', back_populates='tasks')
    user = relationship('User', back_populates='tasks')


class Report(Base):
    __tablename__ = 'reports'
    report_id = Column(Integer, primary_key=True)
    report_name = Column(String)
    organization_id = Column(Integer, ForeignKey('organizations.organization_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    creation_date = Column(Date)
    report_data = Column(String)

    organization = relationship('Organization', back_populates='reports')
    user = relationship('User', back_populates='reports')


engine = create_engine('sqlite:///optibiz.db')
Base.metadata.create_all(engine)
