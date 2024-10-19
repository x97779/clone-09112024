from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction_DBS",methods=["GET","POST"])
def prediction_DBS():
    q = float(request.form.get("q"))
    return(render_template("prediction_DBS.html",r=90.2+(-50.6*q)))

if __name__ == "__main__":
    app.run()

