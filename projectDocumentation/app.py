from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta, timezone
import random

# Flask app and database setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'very_secret_key'
db = SQLAlchemy(app)


# User database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    major = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(100))


# Registration page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))

        full_name = request.form['full_name']
        major = request.form['major']
        password = request.form['password']
        email = request.form['email']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(full_name=full_name, major=major, username=username, password_hash=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            session['user_id'] = user.id
            code = random.randint(1000000000, 9999999999)
            send_email(user.email, f"Your verification code is: {code}")
            session['code'] = str(code)
            session['code_time'] = datetime.now(timezone.utc)
            return redirect(url_for('verify'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


# Verification page
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_code = request.form['code']
        if 'code' in session and 'code_time' in session:
            if (datetime.now(timezone.utc) - session['code_time']) < timedelta(minutes=10) and session['code'] == user_code:
                return 'All good! Welcome to use our service!'
            else:
                flash('Invalid or expired code')
        return redirect(url_for('verify'))
    return render_template('verify.html')


# Function to send email using smtplib
def send_email(email, message):
    sender_email = "Insert Email" **ADD EMAIL HERE**
    password = "rszq jxne iatf yrty"
    msg = MIMEText(message)
    msg['Subject'] = 'Your Login Code'
    msg['From'] = sender_email
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, msg.as_string())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
