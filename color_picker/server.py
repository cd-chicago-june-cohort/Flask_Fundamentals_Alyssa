from flask import Flask, render_template, request, redirect

app = Flask(__name__)
color = "html{background-color: rgb(255,255,255);}"

@app.route('/', methods=['POST', 'GET'])
def index():
    print request.method
    if request.method == 'POST':
        red = request.form['red']
        green = request.form['green']
        blue = request.form['blue']
        color = "html{background-color: rgb(" + red + ',' + green + ',' + blue + ");}"
        return render_template('index.html', color=color)
    else:
        return render_template('index.html')

app.run(debug=True)