# -*- coding: utf-8 -*-
# Python3
# Sample of Flask Web Application
from datetime import datetime
import logging
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response


app = Flask(__name__)

# Custom Jinja Filter.
app.jinja_env.filters['sn'] = lambda str_:str_ if str_ != None else ''


@app.route('/')
def index():
    userName = None
    totalPay = 0
    return render_template('index.html', 
        message="Hello", userName=userName, totalPay=totalPay)

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

@app.route("/cookie")
def cookie():
    # Contents
    response = make_response("OK")
    # Create cookie
    max_age = 60 * 60 * 24 * 30 # 30 days
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie("gscookie", value="valval", expires=expires)
    # Response
    return response

@app.route("/get_from_cookie")
def get_from_cookie():
    val = request.cookies.get("gscookie")
    return val

app.secret_key = 'my_special_secret_key'

@app.route("/session")
def session_sample():
    val = int(session.get("num", 1))
    session["num"] = val + 1
    return "%d回目の訪問ですね！" % val

info_handler = logging.FileHandler('info.log')
info_handler.setLevel(logging.INFO)
app.logger.addHandler(info_handler)

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.ERROR)
app.logger.addHandler(error_handler)

@app.route("/logging")
def logging_sample():
    app.logger.info('Info log...')
    app.logger.warning('Warning log...')
    app.logger.error('Error log...')
    try:
        1 / 0
    except:
        app.logger.exception("Exception log...")
    # Response.
    return "ok"

# The sample of Blueprint.
from api import app as api_app
app.register_blueprint(api_app)

if __name__ == "__main__":
    app.run(debug=True)