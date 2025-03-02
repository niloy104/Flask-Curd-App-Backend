# Flask Curd Application

![Flask](https://img.shields.io/badge/Flask-1.1.2-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)

A simple Flask-based application that provides user authentication and student management functionalities using an SQLite database. It supports user registration, login, logout, and CRUD operations for student records.

## Features
- User authentication (register, login, logout)
- CRUD operations for student records
- Secure password hashing
- Session management with Flask

## Dependencies
The application requires the following Python modules:
- `Flask` - For creating the web application.
- `flask_sqlalchemy` - For database management.
- `hashlib` and `os` - For password hashing and verification.

## Setup
To set up the application, follow these steps:

1. **Clone the repository**
   ```sh
   git clone https://github.com/niloy104/Flask-Curd-App-Backend.git
   cd flask-app
   ```
2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Initialize the database**:
   ```sh
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```
5. **Run the application**:
   ```sh
   python app.py
   ```
   The server will start in debug mode and be accessible at `http://127.0.0.1:5000/`.

## API Endpoints
### User Authentication
- **`POST /register`** - Registers a new user.
- **`POST /login`** - Authenticates a user and starts a session.
- **`GET /logout`** - Ends the user's session.

### Student Management
- **`GET /`** *(Login Required)* - Retrieves all students.
- **`POST /create`** - Adds a new student.
- **`PUT /edit/<id>`** - Updates a student's information.
- **`DELETE /delete/<id>`** - Removes a student from the database.


### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### 🌟 Found this project helpful?

Give it a star to show your support!
