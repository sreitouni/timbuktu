from journeyapp import app
from journeyapp import db
from flask import redirect, render_template, request, session, url_for,flash
from flask_bcrypt import Bcrypt
import re
import os

# Create an instance of the Bcrypt class, which we'll be using to hash user
# passwords during login and registration.
flask_bcrypt = Bcrypt(app)

USER_ROLE_traveller = 'traveller'
USER_ROLE_EDITOR = 'editor'
USER_ROLE_ADMIN = 'admin'

# Default role assigned to new users upon registration.
DEFAULT_USER_ROLE = USER_ROLE_traveller

# assuming default user status is 'active'.
DEFAULT_USER_STATUS = 'active'

# Status of user account
ACTIVE_STATUS= 'active'
INACTIVE_STATUS= 'banned'

def user_home_url():
    if 'loggedin' in session:
        role = session.get('role', None)

        if role== USER_ROLE_traveller:
            home_endpoint='traveller_home'
        elif role== USER_ROLE_EDITOR:
            home_endpoint='editor_home'
        elif role== USER_ROLE_ADMIN:
            home_endpoint='admin_home'
        else:
            home_endpoint = 'logout'
    else:
        home_endpoint = 'login'
    return url_for(home_endpoint)


@app.route('/traveller/home')
def traveller_home():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('traveller_home.html')

@app.route('/editor/home')
def editor_home():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    return render_template('editor_home.html')


@app.route('/admin/home')
def admin_home():
     if 'loggedin' not in session:
          return redirect(url_for('login'))
     elif session['role']!='admin':
          return render_template('access_denied.html'), 403
     return render_template('admin_home.html')

@app.route('/', endpoint='home')
def root():
    if 'loggedin' in session:
        return redirect(user_home_url())
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page endpoint.

    Methods:
    - get: Renders the login page.
    - post: Attempts to log the user in using the credentials supplied via the
        login form, and either:
        - Redirects the user to their role-specific homepage (if successful)
        - Renders the login page again with an error message (if unsuccessful).
    
    If the user is already logged in, both get and post requests will redirect
    to their role-specific homepage.
    """
    if 'loggedin' in session:
        return redirect(user_home_url())

    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        # Get the login details submitted by the user.
        username = request.form['username']
        password = request.form['password']

        # Attempt to validate the login details against the database.
        with db.get_cursor() as cursor:
            # Try to retrieve the account details for the specified username.
            #
            # Note: we use a Python multiline string (triple quote) here to
            # make the query more readable in source code. This is just a style
            # choice: the line breaks are ignored by MySQL, and it would be
            # equally valid to put the whole SQL statement on one line like we
            # do at the beginning of the `signup` function.
            cursor.execute('''
                           SELECT user_id, username, password_hash, role, status
                           FROM users
                           WHERE username = %s;
                           ''', (username,))
            account = cursor.fetchone()
            
            if account is not None:
                # We found a matching account: now we need to check whether the
                # password they supplied matches the hash in our database.
                password_hash = account['password_hash']
                
                if flask_bcrypt.check_password_hash(password_hash, password):
                    # Password is correct. Save the user's ID, username, and role
                    # as session data, which we can access from other routes to
                    # determine who's currently logged in.
                    # 
                    # Users can potentially see and edit these details using their
                    # web browser. However, the session cookie is signed with our
                    # app's secret key. That means if they try to edit the cookie
                    # to impersonate another user, the signature will no longer
                    # match and Flask will know the session data is invalid.

                    if account['status'] == INACTIVE_STATUS:
                        return render_template('login.html', 
                                               username=username,
                                               account_inactive=True,
                                               message="Your account currently is banned. Please contact with admin.")
                    else:
                        session['loggedin'] = True
                        session['user_id'] = account['user_id']
                        session['username'] = account['username']
                        session['role'] = account['role']
                        return redirect(user_home_url())
                else:
                    # Password is incorrect. Re-display the login form, keeping
                    # the username provided by the user so they don't need to
                    # re-enter it. We also set a `password_invalid` flag that
                    # the template uses to display a validation message.
                    return render_template('login.html',
                                           username=username,
                                           password_invalid=True)
            else:
                # We didn't find an account in the database with this username.
                # Re-display the login form, keeping the username so the user
                # can see what they entered (otherwise, they might just keep
                # trying the same thing). We also set a `username_invalid` flag
                # that tells the template to display an appropriate message.
                #
                # Note: In this example app, we tell the user if the user
                # account doesn't exist. Many websites (e.g. Google, Microsoft)
                # do this, but other sites display a single "Invalid username
                # or password" message to prevent an attacker from determining
                # whether a username exists or not. Here, we accept that risk
                # to provide more useful feedback to the user.
                return render_template('login.html', 
                                       username=username,
                                       username_invalid=True)

    # This was a GET request, or an invalid POST (no username and/or password),
    # so we just render the login form with no pre-populated details or flags.
    return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if 'loggedin' in session:
         return redirect(user_home_url())
    
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form and 'confirm_password' in request.form:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        location = request.form['location']

        username_error = None
        email_error = None
        password_error = None
        confirm_password_error = None
        first_name_error = None
        last_name_error = None
        location_error = None

        with db.get_cursor() as cursor:
            cursor.execute('SELECT user_id FROM users WHERE username = %s;',
                           (username,))
            account_already_exists = cursor.fetchone() is not None

        with db.get_cursor() as cursor2:
            cursor2.execute('SELECT user_id FROM users WHERE email = %s;',
                           (email,))
            email_already_exists = cursor2.fetchone() is not None
        
        if not username:
            username_error = "Username is required."
        elif account_already_exists:
            username_error = 'An account already exists with this username.'
        elif len(username) > 20:
            username_error = 'Your username cannot exceed 20 characters.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            username_error = 'Your username can only contain letters and numbers.'     
   
        if not email:
            email_error = "Email is required."
        elif email_already_exists:
            email_error = "An account already exists with this email."
        elif len(email) > 320:
            email_error = 'Your email address cannot exceed 320 characters.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            email_error = 'Invalid email address.'        

        if not password:
            password_error = "Password is required."
        elif len(password) < 8:
            password_error = 'Please choose a longer password!'
        elif not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', password):
            password_error = 'Password must contain at least one number, one lowercase letter, and one uppercase letter.'

        if password != confirm_password:
            confirm_password_error = 'Passwords do not match.'

        if first_name:
            if len(first_name) > 50:
                first_name_error = 'Your first name cannot exceed 50 characters.'
            elif not re.match(r"^[A-Za-z'-]+$", first_name):
                first_name_error = 'Your first name can only contain letters.'            

        if last_name:
            if len(last_name) > 50:
                last_name_error = 'Your last name cannot exceed 50 characters.'
            elif not re.match(r"^[A-Za-z'-]+$", last_name):
                last_name_error = 'Your last name can only contain letters.'

        if location:
            if len(location) > 50:
                location_error = 'Your location cannot exceed 50 characters.'            

        if (username_error or email_error or password_error or confirm_password_error or first_name_error or last_name_error or location_error):
            return render_template('signup.html',
                                   username=username,
                                   email=email,
                                   first_name=first_name,
                                   last_name=last_name,
                                   location=location,
                                   password=password,
                                   username_error=username_error,
                                   email_error=email_error,
                                   password_error=password_error,
                                   confirm_password_error=confirm_password_error,
                                   first_name_error=first_name_error,
                                   last_name_error=last_name_error,
                                   location_error=location_error)
        else:
            password_hash = flask_bcrypt.generate_password_hash(password)

            with db.get_cursor() as cursor:
                cursor.execute('''
                               INSERT INTO users (username, password_hash, email, first_name, last_name, location, role, status)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                               ''',
                               (username, password_hash, email, first_name or None, last_name or None, location or None, DEFAULT_USER_ROLE, DEFAULT_USER_STATUS))
            
            return render_template('signup.html', signup_successful=True)    

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    return redirect(url_for('login'))
