# This script runs automatically when our `journeyapp` module is first loaded,
# and handles all the setup for our Flask app.
# Include all modules that define our Flask route-handling functions.
from flask import Flask

app = Flask(__name__)
app.secret_key = 'random-key'

from tapp import connect
from tapp import db
db.init_db(app, connect.dbuser, connect.dbpass, connect.dbhost, connect.dbname)

# Include all modules that define our Flask route-handling functions.
from tapp import user
from tapp import manage
from tapp import manage_users
from tapp import journeys
from tapp import journeys_feed
from tapp import events
from tapp import errors



