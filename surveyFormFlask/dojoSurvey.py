from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "WhyOhWhy"

@app.route('/')
def landing():
    return render_template("survey.html")

@app.route('/results', methods=['POST'])
def results():
    Name = request.form['Name']
    Location = request.form['Location']
    Language = request.form['Language']
    Comments = request.form['Comments']
    if len(Name) < 1:
        flash('Name cannot be empty')
        return render_template('survey.html')
    if len(Comments) >= 120:
        flash('Comment too long')
        return render_template('survey.html')
    return render_template('results.html', Name=request.form['Name'], Location=request.form['Location'], Language=request.form['Language'], Comments=request.form['Comments'])

app.run(debug=True)