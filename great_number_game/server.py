from flask import Flask, render_template, request, redirect, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "a7656fafe94dae72b1e1487670148412"

@app.route('/')
def index():
    if 'secret_number' not in session:
        session['secret_number'] = random.randrange(1,101)
    return render_template('index.html')

@app.route('/process/<guess>')
def process(guess):
    guess = int(guess)
    print guess
    print session['secret_number']
    if guess > session['secret_number']:
        feedback = "Too High"
    elif guess < session['secret_number']:
        feedback = "Too Low"
    elif guess == session['secret_number']:  
        feedback = str(session['secret_number']) + " was the number!"
    return jsonify(feedback=feedback)

@app.route('/again')
def again():
    session.pop('secret_number')
    return redirect ('/')

app.run(debug=True)