from flask import redirect, request, render_template, url_for
from app import my_app, db

@my_app.route('/')
def index():
    return render_template('index.html')


