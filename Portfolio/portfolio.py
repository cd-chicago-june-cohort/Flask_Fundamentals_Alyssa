from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def root_page():
    return render_template('index.html')

@app.route('/projects')

def projects_page():
    return render_template('projects.html')

@app.route('/about')

def about_page():
    return render_template('about.html')

app.run(debug=True)