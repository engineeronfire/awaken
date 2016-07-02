# awaken
#our cloth brand 'awaken' website

1.create a Python virtual enviroment:
    python 3.4:
        $python -m venv flask
    python 2.x:
        $sudo apt install python-virtualenv
        $virtualenv flask

2.install flask and packages:
    $ flask/bin/pip install flask
    $ flask/bin/pip install flask-login
    $ flask/bin/pip install flask-openid
    $ flask/bin/pip install flask-mail
    $ flask/bin/pip install flask-sqlalchemy
    $ flask/bin/pip install sqlalchemy-migrate
    $ flask/bin/pip install flask-whooshalchemy
    $ flask/bin/pip install flask-wtf
    $ flask/bin/pip install flask-babel
    $ flask/bin/pip install guess_language
    $ flask/bin/pip install flipflop
    $ flask/bin/pip install coverage

3. create our website.

    The app folder will be where we will put our application package.
    The static sub-folder is where we will store static files like images, javascripts, and cascading style sheets. 
    The templates sub-folder is obviously where our templates will go.

