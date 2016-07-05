from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
#The two route decorators above the function create the mappings
#from URLs / and /index to this function.
@app.route('/')
@app.route('/index')

def index():
    user = {'nickname':'HARRY'} #fake user
    posts = [
        {
            'author': {'nickname':'jhon'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'balalala'
        }
    ]
    # This function takes a template filename and a variable list of template arguments 
    #and returns the rendered template, with all the arguments replaced
    #the render_template function invokes the Jinja2 templating engine that is part of the Flask framework.
    #Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments.
    #The Jinja2 templates also support control statements, given inside {%...%} blocks.
    return render_template('index.html',
                            title=None,
                            user=user,
                            posts=posts)

@app.route('/contact')

def contact():
    return render_template('contact.html',
                            title='Sign In')
# we have imported our LoginForm class, instantiated an object from it,
#and sent it down to the template. This is all that is required to get form fields rendered.
#the methods argument in the route decorator.
#This tells Flask that this view function accepts GET and POST requests.
#Without this the view will only accept GET requests. We will want to receive the POST requests, 
#these are the ones that will bring in the form data entered by the user.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
# If you call it when the form is being presented to the user
#(i.e. before the user got a chance to enter data on it) then it will return False
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s". remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
# redirect. This function tells the client web browser to navigate to a different page instead of the one requested.
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])


