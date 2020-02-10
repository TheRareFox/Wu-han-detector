from flask import Flask,render_template,request,redirect
import sqlite3

app = Flask(__name__)



@app.route('/')
def index(risk = None):
    if risk:
        print(risk)
        return render_template("index.html", risk = risk)
    return render_template("index.html")

@app.route('/submit')
def submit():
    temp = request.args.get('temp')
    risk = 2 if float(temp)>=38.0 else 1
    if request.args.get('travel'):
        risk += 1
    elif request.args.get('cough'):
        risk += 1
    elif request.args.get('breath'):
        risk += 1
    elif request.args.get('eat'):
        risk += 1
    return index(risk)

if __name__ == "__main__":
    app.run(debug = True)