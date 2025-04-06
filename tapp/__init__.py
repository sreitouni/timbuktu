from flask import Flask

app = Flask(__name__)
app.secret_key = 'random-key'

# Import connect directly without circular reference
from tapp.connect import (
    dbuser as connect_dbuser,
    dbpass as connect_dbpass,
    dbhost as connect_dbhost,
    dbname as connect_dbname
)

# Initialize database
from tapp.db import init_db
init_db(app, connect_dbuser, connect_dbpass, connect_dbhost, connect_dbname)

# Import routes
from tapp import (
    user,
    manage,
    journeys,
    errors,
    journeys_feed,
    events,
    manage_users
)