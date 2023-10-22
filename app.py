from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Comece')
def comece():
    return render_template('comece.html')

@app.route('/Consultoria')
def consultoria():
    return render_template('consultoria.html')

@app.route('/Login')
def login():
    return render_template('login.html')

