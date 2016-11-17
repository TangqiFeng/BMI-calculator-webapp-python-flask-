from flask import Flask,render_template,url_for,flash,request

import sqlite3


app = Flask(__name__)
app.secret_key='123'

@app.route('/')
def hello_world():
    mainJs=url_for("static",filename="js/main_part.js")
    loginButton=url_for("static",filename="images/loginButton.png")
    login=url_for("static",filename="images/login.jpg")
    return render_template("index.html",mainJs=mainJs,loginButton=loginButton,login=login)



@app.route('/login', methods=['POST'])

def login():
    mainJs=url_for("static",filename="js/main_part.js")
    convertJs=url_for("static",filename="js/convert.js")
    loginButton=url_for("static",filename="images/loginButton.png")
    login=url_for("static",filename="images/login.jpg")
    form = request.form
    username = form.get('username')
    password = form.get('password')
    
    
    if not username:
        flash("please input username !")
        return render_template("index.html",convertJs=convertJs,mainJs=mainJs,loginButton=loginButton,login=login)
    elif not password:
        flash("please input password !")
        return render_template("index.html",convertJs=convertJs,mainJs=mainJs,loginButton=loginButton,login=login)
    else:
        sql = 'SELECT * FROM mytable'
        conn = sqlite3.connect('data/data.db')
        cur = conn.cursor()
        rows = cur.execute(sql)
        
        conn.commit()
        
        for row in rows:
            un = row[1]
            pw = row[2]
            if (username == un and password == pw):
                flash(row[1])
                return render_template("logined.html",convertJs=convertJs,mainJs=mainJs,loginButton=loginButton,login=login)
                cur.close()
                conn.close()
        
        flash("user name or password is wrong !")
        return render_template("index.html",convertJs=convertJs,mainJs=mainJs,loginButton=loginButton,login=login)
        cur.close()
        conn.close()
            
@app.route('/register')
def registerNow():
    registerButton=url_for("static",filename="images/registerButton.png")
    register=url_for("static",filename="images/register.png")
    return render_template("register.html",registerButton=registerButton,register=register)
    
@app.route('/register', methods=['POST'])
def register():
    registerButton=url_for("static",filename="images/registerButton.png")
    register=url_for("static",filename="images/register.png")
    form = request.form
    username = form.get('username')
    password = form.get('password')
    
    if not username:
        flash("please input username !")
        return render_template("register.html",registerButton=registerButton,register=register)
    elif not password:
        flash("please input password !")
        return render_template("register.html",registerButton=registerButton,register=register)
    else:
        sql = str('INSERT INTO mytable(name,password) VALUES (?,?)')
        conn = sqlite3.connect('data/data.db')
        cur = conn.cursor()
        cur.execute(sql,(username,password))
        conn.commit()
        cur.close()
        conn.close()
        flash("success !")
        return render_template("register.html",registerButton=registerButton,register=register)
    
@app.route('/history', methods=['POST'])
def showHistory():
    form = request.form
    BMI = form.get('bmi')
    
    return BMI

if __name__ == '__main__':
    app.run()