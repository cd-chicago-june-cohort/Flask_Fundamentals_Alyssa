from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def tmnt():
    return render_template('ninja.html', ninja_color=None)

@app.route('/ninja/<ninja_color>')
def turtles(ninja_color):
    return render_template('ninja.html', ninja_color=ninja_color)
            

app.run(debug=True)