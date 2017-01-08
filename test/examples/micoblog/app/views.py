from flask import render_template, redirect, flash
from . import app
from forms import LoginForm


# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Miguel'}
#     posts = [  # fake array of posts
#         {
#             'author': {'nickname': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'nickname': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', user=user, posts=posts)


#  @app.route('/login', methods=['GET', 'POST'])
#  def login():
    #  form = LoginForm()
    #  if form.validate_on_submit():
        #  flash("dd")
        #  return redirect('/index')
    #  return render_template('login.html', title='Sign IN', form=form,
                           #  providers = app.config['OPENID_PROVIDERS'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html')