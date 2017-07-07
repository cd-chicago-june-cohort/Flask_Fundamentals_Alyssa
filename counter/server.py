from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key="ThisIsSecret"

session = {'counter': 0}

@app.route('/')
def index():
    session["counter"] += 1
    print session['counter']
    return render_template('index.html', counter=session['counter'])

@app.route('/modify/<modify>')
def twice(modify):
    if modify == '+2':
        session["counter"] += 1
        print session['counter']
        return redirect('/')
    if modify == 'reset':
        session['counter'] = 0
        print session['counter']
        return redirect('/')

app.run(debug=True)