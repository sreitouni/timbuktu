from journeyapp import app
from journeyapp import db
from flask import redirect, render_template, request, session, url_for,flash
from flask_bcrypt import Bcrypt
import re
import os

@app.route('/manage_users', methods=['GET'])
def manage_users():
    if 'loggedin' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    user_id = session['user_id']
    # Get all the users.
    with db.get_cursor() as cursor:
        cursor.execute("SELECT user_id, username,first_name,last_name, role, status FROM users")
        users = cursor.fetchall()
    return render_template('manage_users.html', users=users,user_id=user_id)


@app.route('/change_user_role/<int:user_id>', methods=['GET','POST'])
def change_user_role(user_id):
    if 'loggedin' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    # Get new role from form.
    new_role = request.form.get('new_role')
    
    if new_role in ['traveller', 'editor', 'admin']:
        with db.get_cursor() as cursor:
            cursor.execute('UPDATE users SET role = %s WHERE user_id = %s;', (new_role, user_id))
        flash(f"User role changed to {new_role} now!", "success")
    # When role be removed, the role will be set to traveller.
    else:
        with db.get_cursor() as cursor:
            cursor.execute('UPDATE users SET role = "traveller" WHERE user_id = %s;', (user_id,))
        flash(f"User role removed, new role is traveller now!", "success")
    return redirect(url_for('manage_users'))


@app.route('/change_user_status/<int:user_id>',methods=['GET', 'POST'])
def change_user_status(user_id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    new_status= request.form.get('new_status')
    if new_status in ['active', 'blocked', 'banned']:
        with db.get_cursor() as cursor:
            cursor.execute('UPDATE users SET status = %s WHERE user_id = %s;', (new_status, user_id))
        flash(f"User status changed to {new_status} now!", "success")
    return redirect(url_for('manage_users'))




# @app.route('/search_users', methods=['GET', 'POST'])
# def managing_users():
#     if 'loggedin' not in session:
#         return redirect(url_for('login'))
    
#     # Get search input from form
#     search_query = request.form.get('search', '')

#     with db.get_cursor() as cursor:
#         cursor.execute('''
#             SELECT user_id, username, first_name, last_name, role, status
#             FROM users
#             WHERE username LIKE %s OR first_name LIKE %s OR last_name LIKE %s
#         ''', (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
#         users = cursor.fetchall()
#     return render_template('search_users.html', users=users, search_query=search_query)