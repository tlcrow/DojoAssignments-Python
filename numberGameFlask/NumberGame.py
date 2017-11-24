from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ItIsFriday'

@app.route('/')
def counter():
    session['count'] = random.randrange(0,101)
    print session['count']
    return render_template("NumberGame.html")

@app.route('/game', methods=["POST"])
def game():
    guess = int(request.form['guess'])
    status = "none"
    if guess > session['count']:
        status = "high"
    elif guess < session['count']:
        status = "low"
    elif guess == session['count']:
        status = "correct"
    print status
    return render_template("game.html", status = status)

@app.route('/reset', methods=["POST"])
def reset():
    session['count'] = random.randrange(0,101)
    return render_template("NumberGame.html")

app.run(debug=True)