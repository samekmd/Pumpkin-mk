from flask import Flask, render_template, request, url_for, jsonify

# from flask_mysqldb import MySQL  

# app.config['MYSQL_Host'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '1938'
# app.config['MYSQL_DB'] = 'login'

# mysql = MySQL(app)


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

@app.route('/Login', methods=('GET', 'POST'))
def login():
    # if request.method == 'POST': 
    #         nome = request.method['nome']
    #         senha = request.method['senha']
    #         cur = mysql.connection.cursor()
    #         cur.execute("INSERT INTO login(nome,senha), VALUES (%s, %s)",(nome,senha))

    #         mysql.connection.commit()
            
    #         cur.close()
             
    #         return 'Dados Salvos com Sucesso!'
        
    return render_template('login.html')

