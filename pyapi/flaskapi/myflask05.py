#!/usr/bin/python3
#imports
from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql
app = Flask(__name__)

#decorator
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/enternew")
def new_wish():
    return render_template("wish.html")

# adding record/creatind table here
@app.route ("/addrec", methods=["POST","GET"])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form["nm"]
            country = request.form["country"]
            des = request.form["des"]

            with sql.connect("database.db")as con:
                cur =con.cursor()
                con.execute('''CREATE TABLE IF NOT EXISTS WISHLIST                        (NAME      TEXT  NOT NULL,
                COUNTRY    TEXT  NOT NULL, 
                DESCRIPTION  TEXT  NOT NULL);''')
                cur =con.cursor()
                cur.execute("INSERT INTO wishlist (name,country,description) VALUES (?,?,?)",(nm,country,des))
                con.commit()
                msg = "Wishlist Added successfully "

        except:
                con.rollback()
                msg= "error in insertOperation"
            
        finally:
                return render_template("result.html",msg=msg)
                con.close()
# Route for List 
@app.route('/list')
def list():
    #Connecting  TO DB
    con = sql.connect("database.db")
    con.row_factory= sql.Row
    cur= con.cursor()
    cur.execute("select * from wishlist")
    rows = cur.fetchall();
    return render_template("list.html",rows=rows)

if __name__ == "__main__":
    app.run(host= "0.0.0.0",port=2224)
