# 2FA Documentation

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

## Known Weaknesses and Future Improvements

While this two-factor authentication system demonstrates core authentication and email verification concepts, there are several areas where the application could be improved for security, scalability, and maintainability.

### Current Weaknesses

- **Hardcoded Secrets**: The application currently stores sensitive information (e.g., email credentials, secret key) directly in the source code. This poses a serious security risk if the code is ever exposed or pushed to a public repository.
- **No CSRF Protection**: The application lacks Cross-Site Request Forgery protection, leaving it vulnerable to malicious form submissions from external sites.
- **No Input Validation**: User inputs (e.g., registration fields, verification codes) are not validated for format, length, or malicious characters. This could lead to unexpected behavior or security issues.
- **No Rate Limiting**: There are no protections against brute-force attacks on login or verification forms, meaning attackers could repeatedly guess credentials or verification codes.
- **Session Management**: Sessions do not expire after authentication, and there is no logout functionality to allow users to terminate their session manually.
- **Email Spoofing or Abuse**: Email is sent using plain SMTP without verification of sender identity, and the email credentials are stored insecurely.
- **No HTTPS Enforcement**: Without HTTPS, credentials and codes could be intercepted on unencrypted connections.
- **Limited User Feedback**: The app does not differentiate between errors (e.g., expired code vs. wrong code), nor does it include user-facing session timers or feedback mechanisms.

### Suggested Future Enhancements

- **Use Environment Variables**: Store secret keys, email credentials, and database URIs securely using environment variables and a `.env` file (with `python-dotenv`).
- **Implement CSRF Protection**: Add CSRF tokens using `Flask-WTF` to protect form submissions.
- **Add Input Validation**: Use `WTForms` or backend checks to validate input fields for expected length, format, and type.
- **Introduce Rate Limiting**: Use `Flask-Limiter` or similar tools to limit login and verification attempts.
- **Secure Session Handling**: Add logout functionality and clear sessions after verification; configure cookies with secure flags (`Secure`, `HttpOnly`, `SameSite`).
- **Enable HTTPS**: Enforce HTTPS in production using a reverse proxy like Nginx or use platforms like Heroku with SSL built in.
- **Integrate Logging and Alerts**: Track failed login attempts, suspicious behavior, and system errors to help detect and respond to threats.
- **Support for Production Deployment**: Add a proper `requirements.txt`, `.gitignore`, and deployment configuration (e.g., Gunicorn for production server).
- **User Experience Improvements**: Add session timeout messages, resend verification code options, and password strength indicators during registration.



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
