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

def login():
    form = LoginForm()
    return render_template('login.html',
                            title='Sign In',
                            form=form)
