from . import app
from flask import render_template, flash, redirect
from forms import LonginForm


@app.route('/')
@app.route('/index')
def index():
    return 'index'


@app.route('/login', methods=['POST'])
def login():
    form = LonginForm()
    if form.validate_on_submit():
        flash("flash")
        return redirect('/index')
    return render_template('login.html',
                           form=form)
