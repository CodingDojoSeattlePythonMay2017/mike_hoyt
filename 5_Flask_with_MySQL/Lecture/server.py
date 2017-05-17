from flask import Flask, render_template, redirect
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, "twitter")

@app.route('/')
def index():
    users_from_db = mysql.query_db("SELECT * FROM users")
    return render_template("index.html", users = users_from_db)

@app.route('/user/<id>')
def show(id):
    user = mysql.query_db("SELECT * FROM users WHERE id = {}".format(id))
    print user
    return render_template("show.html", user = user[0])

app.run(debug=True)
