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
    return 'Hello World'

@app.route('/user/<username>')
def user(username):
    return 'User: %s' % username

@app.route('/post/<int:postid>')
def post(postid):
    return 'Thanks post: id = %d' % postid

if __name__ == "__main__":
    app.run(debug=True)