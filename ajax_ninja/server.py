from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja_color', methods=['POST'])
def ninja_color():
    color = request.form['color']
    print color
    return redirect('/')

app.run(debug=True)