# 2FA Documentation

## 2FA Setup and files

[Project Setup and Files](https://github.com/EthanBByrd/2FactorAuthentication)
- Use this link to look at the project files and how to clone this GitHub Repo

## Project Overview and Purpose

This project is a secure web application built with Python and Flask that implements two-factor authentication (2FA). The system enhances standard login security by requiring users to verify a randomly generated 10-digit code sent to their email after entering valid credentials.

## Purpose

The purpose of this application is for me to demonstrate how to integrate multi-step authentication into a web application. I designed this as a starter project to learn more aboutweb security, user authentication, and full-stack development with Flask.

## Features

- **User Registration**: Users can register with a full name, major, username, password, and email. Passwords are hashed before storage, and duplicate usernames are prevented.
- **User Login**: Users log in using their username and password. Authentication checks are performed securely using hashed values.
- **Email Verification**: Upon successful login, a 10-digit verification code is generated and emailed to the user. The code is valid for 10 minutes.
- **Code Verification**: Users must enter the correct verification code on a separate page to gain access.

## Cybersecurity Ideals

This application is designed with core cybersecurity principles in mind, particularly the **CIA Triad**, which stands for **Confidentiality**, **Integrity**, and **Availability**. These three pillars guide the secure handling of data throughout the authentication process.

### Confidentiality

- User passwords are securely hashed using `bcrypt` before being stored in the database, protecting them from exposure.
- Verification codes are sent only to the registered email address associated with each account, reducing the risk of unauthorized access.
- The use of two-factor authentication adds an extra layer of protection, ensuring that even if login credentials are compromised, access cannot be gained without the email verification code.

### Integrity

- Verification codes are randomly generated and time-limited (valid for 10 minutes), reducing the risk of code reuse or tampering.
- Inputs are validated on both client and server sides to prevent injection attacks and ensure data consistency.
- The system only permits access after both the password and email code have been correctly validated, ensuring data and session integrity.

### Availability

- The application architecture is modular and can be easily extended or scaled to handle more users or additional features.
- Proper error handling is implemented to prevent system crashes from invalid inputs or server issues.
- The use of lightweight tools like Flask and SQLite (or other databases) allows for quick recovery and deployment in various environments.



## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- bcrypt
- smtplib and MIMEText (for sending email)

## File Overview

- `app.py`: Main backend application logic.
- `templates/login.html`: Login page.
- `templates/register.html`: Registration page.
- `templates/verify.html`: Code verification page.
- `README.md`: Project documentation.




