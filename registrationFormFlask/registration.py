from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "WhyOhWhy"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def landing():
    return render_template("registration.html")

@app.route('/results', methods=['POST'])
def results():
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    Email = request.form['Email']
    Password = request.form['Password']
    Confirm_Password = request.form['Confirm_Password']
    
    if len(First_Name) < 1:
        flash('First Name cannot be empty')
        return render_template('registration.html')
    if not First_Name.isalpha():
        flash('First Name cannot contain numbers')
        return render_template('registration.html')
    if not Last_Name.isalpha():
        flash('Lirst Name cannot contain numbers')
        return render_template('registration.html')
    if len(Last_Name) < 1:
        flash('Last Name cannot be empty')
        return render_template('registration.html')
    if len(Email) < 1:
        flash("Email cannot be blank!")
        return render_template('registration.html')
    elif not EMAIL_REGEX.match(request.form['Email']):
        flash("Invalid Email Address!")
        return render_template('registration.html')
    if len(Password) < 8:
        flash("Must be longer than 8 characters")
        return render_template('registration.html')
    if len(Confirm_Password) < 8:
        flash("Must be longer than 8 characters")
        return render_template('registration.html')
    if Password != Confirm_Password:
        flash("Passwords must match")
        return render_template('registration.html')
    
    return render_template('results.html', First_Name=First_Name, Last_Name=Last_Name, Email=Email, Password=Password, Confirm_Password=Confirm_Password)

app.run(debug=True)