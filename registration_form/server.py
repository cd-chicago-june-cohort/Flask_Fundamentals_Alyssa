from flask import Flask, render_template, redirect, flash, request, session
import re

app = Flask(__name__)
app.secret_key= "key"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    error=False
    # All fields are required and must not be blank
   
    if len(email)<1 or len(first_name)<1 or len(last_name)<1 or len(password)<1 or len(confirm_password)<1:
        flash("All fields are required!", 'red')
        error=True
    # First and Last Name cannot contain any numbers
    if not first_name.isalpha() or not last_name.isalpha():
        flash("Names cannot contain numbers or symbols", 'red')
        error=True
    # Password should be more than 8 characters
    if len(password)<9:
        flash("Passwords must be more than 8 characters", 'red')
        error=True
    # Email should be a valid email
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'red')
        error=True
    # Password and Password Confirmation should match
    if password != confirm_password:
        flash("Passwords do not match!", 'blue')
        error=True
    if not error:
        flash("Thanks for submitting your information", 'success')
    return redirect('/') 
app.run(debug=True)