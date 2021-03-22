from flask import Flask, render_template, request

app = Flask(__name__)

""" Home page which is our index file """
@app.route('/')
def home_page():
    return render_template('index.html')