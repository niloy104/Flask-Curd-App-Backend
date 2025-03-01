from flask import Flask, request, redirect, flash, jsonify, session
from config import Config
from models import db, Student, User
from utils import hash_password, verify_password

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class
app.secret_key = 'samplesecret'  # Secret key for session management

db.init_app(app)  # Initialize the database with the Flask app

# Create database tables within the application context
with app.app_context():
    db.create_all()

# Decorator function to check if a user is logged in
def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Check if user is in session
            return jsonify({'error': 'Please login first'}), 401  # Unauthorized access response
        return f(*args, **kwargs)  # Proceed with the original function
    return decorated_function

# Route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']  # Get username from form data
    password = request.form['password']  # Get password from form data

    # Create new user with hashed password
    user = User(username=username, password=hash_password(password))
    db.session.add(user)
    
    try:
        db.session.commit()  # Commit changes to the database
        flash('User registered successfully!')
    except:
        db.session.rollback()  # Rollback transaction in case of error
        flash('Error: User could not be created!')
    finally:
        return 'Registered API called'  # Return a response

# Route to handle user login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']  # Get username from form data
    password = request.form['password']  # Get password from form data
    
    user = User.query.filter_by(username=username).first()  # Fetch user from database
    if user and verify_password(user.password, password):  # Verify password
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({'message': 'Login successful'})
 
    return jsonify({'error': 'Invalid credentials'}), 401  # Unauthorized response

# Route to handle user logout
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({'message': 'Logout successful'})

# Route to fetch all students (requires login)
@app.route('/', methods=['GET'])
@login_required  # Protect route with login_required decorator
def get():
    students = Student.query.all()  # Fetch all students from the database
    return jsonify([student.to_dict() for student in students])  # Return JSON response

# Route to create a new student record
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']  # Get student name from form data
    email = request.form['email']  # Get student email from form data
    class_name = request.form['class_name']  # Get class name from form data

    student = Student(name=name, email=email, class_name=class_name)
    db.session.add(student)

    try:
        db.session.commit()  # Commit changes to the database
        flash('Student created successfully!')
    except:
        db.session.rollback()  # Rollback transaction in case of error
        flash('Error: Student could not be created!')
    finally:
        return 'Create API called'  # Return a response

# Route to update a student's details
@app.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    student = Student.query.get_or_404(id)  # Fetch student by ID or return 404
    
    student.email = request.form['email']  # Update student email
    student.class_name = request.form['class_name']  # Update student class name
    
    try:
        db.session.commit()  # Commit changes to the database
        flash('Student updated successfully!')
    except:
        db.session.rollback()  # Rollback transaction in case of error
        flash('Error: Student could not be updated!')
    finally:
        return 'Update API called'  # Return a response

# Route to delete a student record
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    student = Student.query.get_or_404(id)  # Fetch student by ID or return 404
    
    try:
        db.session.delete(student)  # Delete student from database
        db.session.commit()  # Commit changes
        flash('Student deleted successfully!')
    except:
        db.session.rollback()  # Rollback transaction in case of error
        flash('Error: Student could not be deleted!')
    finally:
        return 'Delete API called'  # Return a response

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
