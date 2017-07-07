from flask import Flask, render_template, request, redirect, session

import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "d41d8cd98f00b204e9800998ecf273"

@app.route('/')
def index():
    if 'gold_counter' not in session:
        session['gold_counter'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    building = request.form['building']
    # Use random numbers to deterimine how much gold won or lost based on location
    if building == 'farm':
        gold = random.randint(10,20)
    elif building == 'cave':
        gold = random.randint(5,10)
    elif building == 'house':
        gold = random.randint(2,5)
    elif building == 'casino':
        gold = random.randint(-50,50)
    # Update the session gold_counter to reflect the change
    updated_gold = session['gold_counter']
    updated_gold = updated_gold + gold
    session['gold_counter'] = updated_gold
    # Write the activity html
    if gold > 0:
        activity_string = 'Earned {} golds from the {}! ({})'.format(gold, building, time)
        activity_class = 'green'
    elif gold < 0:
        gold = gold * -1
        activity_string = 'Entered a casino and lost {} golds . . . Ouch. ({})'.format(gold, time)
        activity_class='red'
    else:
        activity_string = 'You managed to break even at the casino.  No gold earned or lost!'
        activity_class='blue'
    # Update the session activities list to have the new activity first
    activities = session['activities']
    activity_data = {activity_class:activity_string}
    activities.insert(0, activity_data)
    session['activities'] = activities
    return redirect('/')

app.run(debug=True)