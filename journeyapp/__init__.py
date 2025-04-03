# This script runs automatically when our `journeyapp` module is first loaded,
# and handles all the setup for our Flask app.
# Include all modules that define our Flask route-handling functions.
from flask import Flask
from journeyapp import db
from journeyapp import connect

app = Flask(__name__)

from journeyapp import user
from journeyapp import manage
from journeyapp import journeys
# Set the "secret key" that our app will use to sign session cookies. This can
# be anything.
# 
# Anyone with access to this key can pretend to be signed in as any user. In a
# real-world project, you wouldn't store this key in your source code. To learn
# about how to manage "secrets" like this in production code, check out
# https://blog.gitguardian.com/how-to-handle-secrets-in-python/
#
# For the purpose of your assignments, you DON'T need to use any of those more
# advanced and secure methods: it's fine to store your secret key in your
# source code like we do here.
app.secret_key = 'Example Secret Key (CHANGE THIS TO YOUR OWN SECRET KEY!)'

# Set up database connection.

from journeyapp import connect
from journeyapp import db
db.init_db(app, connect.dbuser, connect.dbpass, connect.dbhost, connect.dbname)

# Include all modules that define our Flask route-handling functions.
from journeyapp import user
from journeyapp import manage
from journeyapp import journeys
from journeyapp import events
from journeyapp import manage_users