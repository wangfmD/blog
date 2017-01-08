# coding=utf-8

from . import app
from flask import render_template, flash, redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('hi hi hi ')
        # return redirect('/index')
        return "helll"
    return render_template('login.html',
                           form=form)
