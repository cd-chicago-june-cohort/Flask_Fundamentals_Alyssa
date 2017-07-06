from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    return '<img src=' + url_for('static', filename='ninjas/tmnt.png') + '>'

@app.route('/ninja/<ninja_color>')
def turtles(ninja_color):
    if ninja_color == 'blue':
        return '<img src=' + url_for('static', filename='ninjas/leonardo.jpg') + '>'
    elif ninja_color == 'orange':    
        return '<img src=' + url_for('static', filename='ninjas/michelangelo.jpg') + '>'
    elif ninja_color == 'red':
        return '<img src=' + url_for('static', filename='ninjas/raphael.jpg') + '>'
    elif ninja_color == 'purple':
        return '<img src=' + url_for('static', filename='ninjas/donatello.jpg') + '>'
    else:
        return '<img src=' + url_for('static', filename='ninjas/notapril.jpg') + '>'
            

app.run(debug=True)