#!/usr/bin/python
from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def guest(guesty):
    return f"Hello {guesty} guest"

@app.route("/user/<name>")
def user(name):
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("guest", guesty= name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
