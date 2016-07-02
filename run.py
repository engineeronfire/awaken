#!flask/bin/python
# imports the app variable from our app package and invokes its run method to start the server.
#Remember that the app variable holds the Flask instance that we created it above.
from app import app
app.run(host='0.0.0.0', port=8888, debug=True)
