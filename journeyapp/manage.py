from journeyapp import app
from journeyapp import db
from flask import redirect, render_template, request, session, url_for,flash
from flask_bcrypt import Bcrypt
import re
import os

# Create an instance of the Bcrypt class, which we'll be using to hash user
# passwords during login and registration.
flask_bcrypt = Bcrypt(app)

#create path for uploading profile images 
UPLOAD_FOLDER = os.path.join(app.root_path, 'static','profile_images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """User Profile page endpoint.

    Methods:
    - get: Renders the user profile page for the current user.

    If the user is not logged in, requests will redirect to the login page.
    """
    #if the user is not logged in, redirect to the login page 
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    #if new details are entered, and method is POST, update the profile
    #only update the profile if the method is POST and all the required fields are filled
    if request.method == 'POST' and 'username' in request.form and 'useremail' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'location' in request.form:
        new_username = request.form['username']
        new_email = request.form['useremail']
        new_first_name = request.form['first_name']
        new_last_name = request.form['last_name']
        new_location = request.form['location']
        new_profile_image = request.files.get('profile_image')

        #Assume no errors are found
        new_username_error = None
        new_email_error = None
        new_first_name_error = None
        new_last_name_error = None
        new_location_error = None
        
        #if user changes the username,check the username is exist
        # #check if the account is already exist in the database 
        if new_username != session['username']:
            with db.get_cursor() as cursor:
                cursor.execute(''' SELECT user_id FROM users WHERE username =%s''', (new_username,))
                account_already_exists = cursor.fetchone() is not None

                if account_already_exists:
                    new_username_error = 'An account with that username already exists.'

        if new_email != request.form.get('email_old'):
            with db.get_cursor() as cursor:
                    cursor.execute(''' SELECT user_id FROM users WHERE email =%s''', (new_email,))
                    email_already_exists = cursor.fetchone() is not None 

                    if email_already_exists:
                        new_email_error = 'The email address is already in use'
        
        #if there is no new username error, means the username is valid or remain the same
        if not new_username_error:
            if len(new_username) > 20:
                new_username_error = 'Your username cannot exceed 20 characters.'
            elif not re.match(r'[A-Za-z0-9]+', new_username):
                new_username_error = 'Your username can only contain letters and numbers.' 

        #check if the email is valid 
        if len(new_email) >320:
            new_email_error = 'Your email address cannot exceed 320 characters.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', new_email):
            new_email_error = 'Invalid email address.'
        
        #check length of first name, last name and location 
        if len(new_first_name) > 50:
            new_first_name_error = 'Your first name cannot exceed 50 characters.'
        
        if len(new_last_name) > 50:
            new_last_name_error = 'Your last name cannot exceed 50 characters.'
        
        if len(new_location) > 50:
            new_location_error = 'Your location cannot exceed 50 characters.'

        #save the new iamge if there is any 
        if new_profile_image and new_profile_image.filename:
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], new_profile_image.filename)
            new_profile_image.save(save_path)
            new_profile_image = os.path.join('profile_images', new_profile_image.filename).replace(os.sep, '/') #load the picture information to the value
        else:
            new_profile_image = request.form.get('profile_image_old')

            if new_profile_image in [None, '', 'None']:
                new_profile_image = None
        
        #in ths case if any errors are found, render the profile page with the error messages and the user's input
        if new_username_error or new_email_error or new_first_name_error or new_last_name_error or new_location_error:

            error_profile = {'username' : new_username,
                            'email' :new_email,
                            'first_name' : new_first_name,
                            'last_name' : new_last_name,
                            'location': new_location,
                            'role': session['role']}
            
            return render_template('profile.html',
                                   profile = error_profile,
                                   new_username_error = new_username_error, 
                                   new_email_error = new_email_error,
                                   new_first_name_error = new_first_name_error,
                                   new_last_name_error = new_last_name_error,
                                   new_location_error = new_location_error
                                   )
        
        '''if no errors are found, update the user's profile '''
        with db.get_cursor() as cursor:
            cursor.execute(''' 
                                UPDATE users 
                               SET username = %s, email=%s, 
                                    first_name=%s, 
                                    last_name=%s, location=%s, 
                                    profile_image=%s
                               WHERE user_id = %s;''', 
                               (new_username, new_email, new_first_name, new_last_name, new_location, new_profile_image,session['user_id']))
                
            cursor.execute('''SELECT username, email, role, first_name, last_name, location, profile_image  
                        FROM users WHERE user_id = %s;''',
                        (session['user_id'],))
            profile = cursor.fetchone()
            return render_template('profile.html',profile=profile, update_successful = True)

    '''if the method is GET only, where the user is not updating profile but just viewing it'''
    with db.get_cursor() as cursor:
        cursor.execute('''SELECT username, email, role, first_name, last_name, location, profile_image 
                        FROM users WHERE user_id = %s;''',
                        (session['user_id'],))
        profile = cursor.fetchone()
    return render_template('profile.html', profile=profile)


#define route for updating password 
@app.route('/change_password', methods=['GET','POST'])
def change_password():
    
    if 'loggedin' not in session: #If the user is not logged in, requests will redirect to the login page.
         return redirect(url_for('login'))
    
    #if request method is POST and new password is in the form, update the password
    if request.method == 'POST' and 'new_password' in request.form and 'new_confirm_password' in request.form:
        with db.get_cursor() as cursor:
            cursor.execute('''SELECT password_hash FROM users WHERE user_id = %s;''', (session['user_id'],))
            password_hash = cursor.fetchone()

        current_password = request.form['current_password']
        new_password = request.form['new_password']
        new_confirm_password = request.form['new_confirm_password']

        current_password_error= None
        new_password_error = None 
        new_confirm_password_error = None

        #check if the current password is valid
        if not flask_bcrypt.check_password_hash(password_hash['password_hash'], current_password):
            current_password_error = 'Your current password is not correct. Please try again.'

        #check password is valid and matching with the confirm password
        if len(new_password)<8:
            new_password_error = " Please choose a longer password"
        elif not re.search(r'[A-Z]', new_password):
            new_password_error = "Your password must contain at least one upercase letter."
        elif not re.search(r'[a-z]', new_password):
            new_password_error = "Your password must contain at least one lowercase letter."
        elif not re.search(r'\d', new_password):
            new_password_error = "Your password must contain at least one digit."
        elif new_password != new_confirm_password:
            new_confirm_password_error = "Your password is not matching, please try again."
        elif flask_bcrypt.check_password_hash(password_hash['password_hash'], new_password):
            new_password_error = 'Your password cannot be the same as your current one.'
        
        #if any errors are found, render the page with the error messages 
        if current_password_error or new_password_error or new_confirm_password_error:
            return render_template('change_password.html', 
                                   current_password_error = current_password_error, 
                                   new_password_error = new_password_error, 
                                   new_confirm_password_error = new_confirm_password_error)
        
        #if no errors are found, update the password
        else:
            new_password_hash = flask_bcrypt.generate_password_hash(new_password)
            with db.get_cursor() as cursor:
                cursor.execute(''' 
                                UPDATE users
                                SET password_hash = %s
                               WHERE user_id = %s;''', (new_password_hash, session['user_id']))
                return render_template('change_password.html', password_updated = True)
    return render_template('change_password.html')

@app.route('/drop_profile_image')
def drop_profile_image():
#Create function to drop user profile image

    with db.get_cursor() as cursor:
        cursor.execute(''' 
                        UPDATE users
                        SET profile_image = NULL
                       WHERE user_id = %s;''', (session['user_id'], ))

    with db.get_cursor() as cursor:
        cursor.execute('''SELECT username, email, role, first_name, last_name, location, profile_image 
                        FROM users WHERE user_id = %s;''',
                        (session['user_id'],))
        profile = cursor.fetchone()
    return render_template('profile.html', profile=profile)

