from flask import Flask
from flask import render_template,request
import sqlite3
import datetime

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    conn = sqlite3.connect('userlog.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now()
    c.execute("insert into user (name,timestamp) values(?,?)", (q,timestamp))
    conn.commit()
    c.close()
    conn.close()
    return(render_template("main.html"))

@app.route("/prediction_DBS",methods=["GET","POST"])
def prediction_DBS():
    q = float(request.form.get("q"))
    return(render_template("prediction_DBS.html",r=90.2+(-50.6*q)))

@app.route("/userlog",methods=["GET","POST"])
def userlog():
    conn = sqlite3.connect('userlog.db')
    c = conn.cursor()
    c.execute("select * from user")
    r=""
    for row in c:
        r=r+str(row)
    c.close()
    conn.close()
    return(render_template("userlog.html",r=r))

if __name__ == "__main__":
    app.run()

