from flask_script import Manager
from webapp import app
import sqlite3

manager = Manager(app)

DATABASE = 'data/data.db'

    
@manager.command
def setup_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('create table mytable(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)')
    conn.commit()
    cur.execute('create table myinfo(id INTEGER, date TEXT, bmi REAL, FOREIGN KEY(id) REFERENCES mytable(id))')
    conn.commit()
    
    cur.execute('INSERT INTO mytable(name,password) VALUES("kyle","123")')
    cur.execute('INSERT INTO mytable(name,password) VALUES("zehua","321")')
    
    conn.commit()
    cur.close()
    conn.close()

    
@manager.command
def query_all():
        
    sql = 'SELECT * FROM mytable'
    conn = sqlite3.connect('data/data.db')
    cur = conn.cursor()
    rows = cur.execute(sql)
    for row in rows:
        print (row[1])
        print (row[2])
    conn.commit()
    cur.close()
    conn.close()
    
    

    
if __name__ == '__main__':
    manager.run()