from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    error = False
    if len(request.form['name']) < 1 or len(request.form['comment']) < 1 :
        error = True
        flash("Fields cannot be left blank!")
    if len(request.form['comment']) > 120:
        error = True
        flash("Please keep comments to 120 characters or less")
    print error
    if error:
        return redirect('/')
    else:
        session['name']=request.form['name']
        session['location']=request.form['location']
        session['language']=request.form['language']
        session['comment']=request.form['comment']
        return redirect('/results_page')
    
    
@app.route('/results_page')    
def results_page():
    return render_template('results.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comment'])

app.run(debug=True)