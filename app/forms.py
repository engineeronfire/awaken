from flask.ext.wtf import Form
#the two form field classes that we need, StringField and BooleanField.
from wtforms import StringField, BooleanField
#The DataRequired import is a validator,
#a function that can be attached to a field to perform validation on the data submitted by the user.
#The DataRequired validator simply checks that the field is not submitted empty.
#There are many more validators included with Flask-WTF,
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

