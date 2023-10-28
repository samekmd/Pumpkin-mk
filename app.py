from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Biotipos')
def comece():
    return render_template('biotipos.html')

@app.route('/Comece')
def consultoria():
    return render_template('comece.html')

@app.route('/Login')
def login():
    return render_template('login.html')

