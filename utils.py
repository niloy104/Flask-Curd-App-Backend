import hashlib
import os

# Function to hash a password with a random salt
def hash_password(password):
    salt = os.urandom(16).hex()  # Generate a random 16-byte salt and convert it to a hex string
    salted_password = password + salt  # Append salt to the password
    hashed = hashlib.sha256(salted_password.encode())  # Hash the salted password using SHA-256
    return f"{salt}:{hashed}"  # Return the salt and hash as a single string

# Function to verify a password by rehashing and comparing with stored hash
def verify_password(db_password, input_password):
    salt, stored_hash = db_password.split(':')  # Split stored hash to get the salt and hash
    salted_password = input_password + salt  # Append salt to input password
    hashed = hashlib.sha256(salted_password.encode())  # Hash the input password with the same salt
    return hashed == stored_hash  # Compare the newly hashed password with the stored hash
