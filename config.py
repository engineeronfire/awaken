#Many Flask extensions require some amount of configuration,
#so we are going to setup a configuration file inside our root microblog folder
#so that it is easily accessible if it needs to be edited

#setting for the Flask-WTF extension
WTF_CSRF_ENABLED = True
SECRET_KEY =  'you-will-never-guess'

#defining the list of OpenID providers that we want to present.
#use this array in login view function
OPENID_PROVIDERS = [

        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'https://www.flickr.com/<username>'},
        {'name': 'MyopenId', 'url': 'https://www.myopenid.com'}]

