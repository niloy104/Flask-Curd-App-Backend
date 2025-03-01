from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance for database operations
db = SQLAlchemy()

# User model representing a user in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(60), unique=True, nullable=False)  # Unique username, required
    password = db.Column(db.String(120), nullable=False)  # Hashed password, required

# Student model representing a student record in the database
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each student
    name = db.Column(db.String(100), nullable=False)  # Student name, required
    email = db.Column(db.String(60), unique=True)  # Unique email for the student
    class_name = db.Column(db.String(60))  # Name of the class the student is enrolled in
    admitted_at = db.Column(db.DateTime, default=datetime.now())  # Admission timestamp, defaults to current time

    # Method to return student data as a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'class_name': self.class_name,
            'admitted_at': self.admitted_at.isoformat() if self.admitted_at else None
        }
