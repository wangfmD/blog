'''
doc
'''
from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LonginForm(Form):
    '''
    doc
    '''
    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)
