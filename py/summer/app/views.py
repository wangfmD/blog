# -*- coding=utf-8 -*-
from flask import render_template, flash
from app import app
from .form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'wfm'}
    posts = [{
        'author': {
            'name': 'wfm'
        },
        'post': 'dasfsadfasfsadf'
    }, {
        'author': {
            'name': 'wzr'
        },
        'post': 'aaaaaaaaaaaaaaaa'
    }]
    return render_template("index.html", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for openid="' + form.openid.data + '",remember='
              + str(form.remember_me.data))
    return render_template("login.html", form=form,
                            providers = app.config['OPENID_PROVIDERS'])