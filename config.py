import os

# Configuration class for the Flask application
class Config:
    SECRET_KEY = 'myownsecretkey'  # Secret key for session management and security
    project_dir = os.path.abspath(os.path.dirname(__file__))  # Get absolute path of the project directory
    
    # Define the database URI using SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(project_dir, 'data', 'data.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to improve performance