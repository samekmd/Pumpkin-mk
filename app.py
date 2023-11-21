from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL 
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy







app = Flask('__name__')



mysql = MySQL(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@localhost/login'
app.config['MYSQL_Host'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# login_manager = LoginManager(app)
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Biotipos')
def comece():
    return render_template('biotipos.html')

@app.route('/Comece')
def consultoria():
    return render_template('comece.html')

@app.route('/Login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST': 
            nome = request.form['nome']
            senha = request.form['senha']
            with app.app_context():
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO login(nome,senha) VALUES (%s, %s)", (nome, senha))

                mysql.connection.commit()
            
                cur.close()
              
            return render_template('dados_salvos.html')
        
    return render_template('login.html')



@app.route('/users')
def users():
     cur = mysql.connection.cursor()

     users = cur.execute("SELECT * FROM login")

     if users > 0:
          userDetails = cur.fetchall()
          
          return render_template("users.html", userDetails=userDetails) 
          

@app.route('/dados_salvos')
def dados_salvos():
     return render_template('dados_salvos.html')
