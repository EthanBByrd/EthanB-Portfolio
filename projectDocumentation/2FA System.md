# 2FA Documentation

## 2FA Setup and files

[Project Setup and Files](https://github.com/EthanBByrd/2FactorAuthentication)
- Use this link to look at the project files and how to clone this GitHub Repo

## Project Overview and Purpose

This project is a secure web application built with Python and Flask that implements two-factor authentication (2FA). The system enhances standard login security by requiring users to verify a randomly generated 10-digit code sent to their email after entering valid credentials.

## Purpose

The purpose of this application is to demonstrate how to integrate multi-step authentication into a web application. It is designed as a learning tool or starter project for developers interested in web security, user authentication, and full-stack development with Flask.

## Features

- **User Registration**: Users can register with a full name, major, username, password, and email. Passwords are hashed before storage, and duplicate usernames are prevented.
- **User Login**: Users log in using their username and password. Authentication checks are performed securely using hashed values.
- **Email Verification**: Upon successful login, a 10-digit verification code is generated and emailed to the user. The code is valid for 10 minutes.
- **Code Verification**: Users must enter the correct verification code on a separate page to gain access.

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




