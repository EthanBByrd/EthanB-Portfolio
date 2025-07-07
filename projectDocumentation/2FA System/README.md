# Two-Factor Authentication System

This repository contains a Python Flask application that implements two-factor authentication using a combination of username-password and email verification. Users must register with their details, log in using their credentials, and verify a randomly generated 10-digit code sent to their email to gain access.

## Files Overview

- `app.py`: The main Python application file containing backend logic.
- `login.html`: HTML template for the login page.
- `register.html`: HTML template for the user registration page.
- `verify.html`: HTML template for the verification page where users input the code received via email.

## Features

- **User Registration**: Users can register by providing their full name, major, username, password, and email. The system checks for duplicate usernames and encrypts passwords before storing them in the database.
- **User Login**: Users log in with their username and password. Authentication is done by comparing the hashed passwords.
- **Email Verification**: Upon successful login, a 10-digit code valid for 10 minutes is generated and sent to the user's registered email address.
- **Code Verification**: Users must enter the received code on the verification page. Access is granted if the code matches and is not expired.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: An ORM for Flask.
- **bcrypt**: For hashing passwords.
- **smtplib and MIMEText**: For sending emails with generated codes.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/two-factor-auth.git
   cd two-factor-auth

pip install flask flask_sqlalchemy bcrypt

python
>>> from app import db
>>> db.create_all()

Within the app.py code, make sure to add the test user email.

