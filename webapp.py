from flask import Flask,render_template,url_for,flash,request

import sqlite3


app = Flask(__name__)
app.secret_key='123'

@app.route('/')
def hello_world():
    indexCss=url_for("static",filename="css/indexCss.css")
    mainJs=url_for("static",filename="js/main_part.js")
    loginButton=url_for("static",filename="images/loginButton.png")
    login=url_for("static",filename="images/login.jpg")
    titlePic=url_for("static",filename="images/title.png")
    ex1=url_for("static",filename="images/ex1.jpg")
    ex2=url_for("static",filename="images/ex2.jpg")
    ex3=url_for("static",filename="images/ex3.png")
    titleBg=url_for("static",filename="images/titleBg.png")
    modelBg=url_for("static",filename="images/modelBg.png")
    bg=url_for("static",filename="images/bg.jpg")
    return render_template("index.html",mainJs=mainJs,indexCss=indexCss,loginButton=loginButton,login=login,titlePic=titlePic,ex1=ex1,ex2=ex2,ex3=ex3,titleBg=titleBg,modelBg=modelBg,bg=bg)



@app.route('/login', methods=['POST'])

def login():
    indexCss=url_for("static",filename="css/indexCss.css")
    loginedCss=url_for("static",filename="css/loginedCss.css")
    mainJs=url_for("static",filename="js/main_part.js")
    convertJs=url_for("static",filename="js/convert.js")
    loginButton=url_for("static",filename="images/loginButton.png")
    login=url_for("static",filename="images/login.jpg")
    titlePic=url_for("static",filename="images/title.png")
    ex1=url_for("static",filename="images/ex1.jpg")
    ex2=url_for("static",filename="images/ex2.jpg")
    ex3=url_for("static",filename="images/ex3.png")
    titleBg=url_for("static",filename="images/titleBg.png")
    modelBg=url_for("static",filename="images/modelBg.png")
    bg=url_for("static",filename="images/bg.jpg")
    form = request.form
    username = form.get('username')
    password = form.get('password')
    
    
    if not username:
        flash("please input username !")
        return render_template("index.html",convertJs=convertJs,indexCss=indexCss,mainJs=mainJs,loginButton=loginButton,login=login,titlePic=titlePic,ex1=ex1,ex2=ex2,ex3=ex3,titleBg=titleBg,modelBg=modelBg,bg=bg)
    elif not password:
        flash("please input password !")
        return render_template("index.html",convertJs=convertJs,indexCss=indexCss,mainJs=mainJs,loginButton=loginButton,login=login,titlePic=titlePic,ex1=ex1,ex2=ex2,ex3=ex3,titleBg=titleBg,modelBg=modelBg,bg=bg)
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
                return render_template("logined.html",convertJs=convertJs,loginedCss=loginedCss,mainJs=mainJs,loginButton=loginButton,login=login,ex3=ex3,titlePic=titlePic,titleBg=titleBg,modelBg=modelBg,bg=bg)
                cur.close()
                conn.close()
        
        flash("user name or password is wrong !")
        return render_template("index.html",convertJs=convertJs,indexCss=indexCss,mainJs=mainJs,loginButton=loginButton,login=login,titlePic=titlePic,ex1=ex1,ex2=ex2,ex3=ex3,titleBg=titleBg,modelBg=modelBg,bg=bg)
        cur.close()
        conn.close()
            
@app.route('/register')
def registerNow():
    registerCss=url_for("static",filename="css/registerCss.css")
    registerBkg=url_for("static",filename="images/registerBg.jpg")
    registerButton=url_for("static",filename="images/registerButton.png")
    register=url_for("static",filename="images/register.png")
    return render_template("register.html",registerCss=registerCss,registerButton=registerButton,register=register,registerBkg=registerBkg)
    
@app.route('/register', methods=['POST'])
def register():
    registerCss=url_for("static",filename="css/registerCss.css")
    registerBkg=url_for("static",filename="images/registerBg.jpg")
    registerButton=url_for("static",filename="images/registerButton.png")
    register=url_for("static",filename="images/register.png")
    form = request.form
    username = form.get('username')
    password = form.get('password')
    
    if not username:
        flash("please input username !")
        return render_template("register.html",registerCss=registerCss,registerButton=registerButton,register=register,registerBkg=registerBkg)
    elif not password:
        flash("please input password !")
        return render_template("register.html",registerCss=registerCss,registerButton=registerButton,register=register,registerBkg=registerBkg)
    else:
        sql = str('INSERT INTO mytable(name,password) VALUES (?,?)')
        conn = sqlite3.connect('data/data.db')
        cur = conn.cursor()
        cur.execute(sql,(username,password))
        conn.commit()
        cur.close()
        conn.close()
        flash("success !")
        return render_template("register.html",registerCss=registerCss,registerButton=registerButton,register=register,registerBkg=registerBkg)
    
@app.route('/moreInfo')
def init():
    registerBkg=url_for("static",filename="images/registerBg.jpg")
    moreInfoCss=url_for("static",filename="css/moreInfoCss.css")
    return render_template("moreInfo.html",moreInfoCss=moreInfoCss,registerBkg=registerBkg);

if __name__ == '__main__':
    app.run()