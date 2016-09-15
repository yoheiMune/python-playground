# -*- coding: utf-8 -*-
# Python3
# Sample of Flask Web Application
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Index Root'
    # flash('Welcome to Flask')
    return render_template('index.html', message="Hello")

@app.route('/hello')
def hello():
    val = request.args.get("msg", "Not defined")
    return 'Hello World '  + val

@app.route('/post_request', methods=['POST'])
def post_request():
    username = request.form["username"]
    return 'Thank you ' + username

# @app.route('/user/<username>')
# def user(username):
#     return 'User: %s' % username

@app.route('/post/<postid>')
def post(postid):
    return 'Thanks post: id = %s' % postid

@app.route('/post2/<int:postid>')
def post2(postid):
    return 'Thanks post: id = %d' % postid

@app.route("/test1")
def test1():
    favs = request.args.getlist("fav")
    print("favs:", favs)
    return "ok"

@app.route("/test2", methods=['POST'])
def test2():
    favs = request.form.getlist("fav")
    print("favs:", favs)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)