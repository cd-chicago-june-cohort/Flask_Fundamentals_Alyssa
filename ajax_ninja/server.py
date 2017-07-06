from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', ninja_color=None)


@app.route('/process/<color>')
def ninjas(color):
    return jsonify(color=color)


app.run(debug=True)