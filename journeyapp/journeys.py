from journeyapp import app
from journeyapp import db
from datetime import datetime, timedelta
from flask import redirect, render_template, request, session, url_for,flash

@app.route('/add_journey', methods=['GET', 'POST'])
def add_journey():
    """
    Add a new journey with title, description and start date.
    """
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    journey_description_error = None
    journey_title_error = None
    journey_start_date_error = None
    # Get info from the form
    if request.method == 'POST' and 'journey_title' in request.form and 'journey_description' and 'journey_start_date' in request.form:
        title = request.form['journey_title']
        description = request.form['journey_description']
        start_date = request.form['journey_start_date']
        user_id = session['user_id']
        
        if not title:
            journey_title_error = 'Please enter journey title.'
        # less than 255 characters
        elif len(title) > 255:
            journey_title_error = 'Title is too long. Please enter a title with less than 255 characters.'
            
        if not description:
            journey_description_error = 'Please enter journey description.'
            
        if not start_date:
            journey_start_date_error = 'Please enter start date.'
        else:
            try:
                parsed_date = datetime.strptime(start_date, '%Y-%m-%d')
                # check if the start date is 100 years ago or 10 years in the future
                if parsed_date < datetime.now() - timedelta(days=36500) or parsed_date > datetime.now() + timedelta(days=3650):
                    journey_start_date_error = 'Please enter a valid start date. It should be within 100 years ago or 10 years in the future.'
            except ValueError:
                journey_start_date_error = 'Invalid date format. Please use DD-MM-YYYY.'
        
        if journey_description_error or journey_title_error or journey_start_date_error:
            return render_template(
                'add_journey.html',
                journey_description=description,
                journey_title=title,
                journey_start_date=start_date,
                journey_description_error=journey_description_error,
                journey_title_error=journey_title_error,
                journey_start_date_error=journey_start_date_error
            )
        # insert new journey to the table
        else:
            with db.get_cursor() as cursor:
                cursor.execute('''
                    INSERT INTO journeys(user_id, journey_title, journey_description, start_date)
                    VALUES (%s, %s, %s, %s);
                ''', (user_id, title, description, start_date))
                flash('Thank you! You journey has been added successfully!', 'success')
                return redirect(url_for('add_journey'))
    return render_template('add_journey.html')


@app.route('/my_journeys', methods=['GET'])
def my_journeys():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id'] 

    with db.get_cursor() as cursor:
        # make journey list ordered by date from newest to oldest.
        cursor.execute('''
            SELECT journey_id, journey_title, journey_description, start_date, status
            FROM journeys
            WHERE user_id = %s
            ORDER BY start_date DESC
        ''', (user_id,))
        journeys = cursor.fetchall()
        # convert datetime to string
        for journey in journeys:
            if isinstance(journey['start_date'], datetime):
                journey['start_date'] = journey['start_date'].strftime('%d-%m-%Y')
    return render_template('my_journeys.html', journeys=journeys)

@app.route('/public_journeys', methods=['GET'])
def public_journeys():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id'] 

    with db.get_cursor() as cursor:
        # get public journey list ordered by date from newest to oldest.
        cursor.execute('''
            SELECT journey_id, journey_title, journey_description, start_date, status
            FROM journeys
            WHERE user_id != %s and status = 'public'
            ORDER BY start_date DESC
        ''', (user_id,))
        journeys = cursor.fetchall()
        # convert datetime to string
        for journey in journeys:
            if isinstance(journey['start_date'], datetime):
                journey['start_date'] = journey['start_date'].strftime('%d-%m-%Y')
    return render_template('public_journeys.html', journeys=journeys)

@app.route('/journey_details/<int:journey_id>', methods=['GET', 'POST'])
def journey_details(journey_id):
    """
    View and update journey details
    """
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    #fetch journey details
    with db.get_cursor() as cursor:
        queryjourney = cursor.execute('SELECT user_id, journey_title, journey_description, start_date, status FROM journeys WHERE journey_id = %s', (journey_id,))
        cursor.execute(queryjourney)
        journey = cursor.fetchone()
    #fetch events associated with this journey
        query_events = cursor.execute('SELECT event_id, event_title, start_date, event_location FROM events WHERE journey_id = %s ORDER BY start_date', (journey_id,))
        cursor.execute(query_events)
        events = cursor.fetchall()
    # check if the user is the owner of the journey
    if(request.method == 'GET'):
        if isinstance(journey['start_date'], datetime):
            journey['start_date'] = journey['start_date'].strftime('%Y-%m-%d')
        is_owner = journey['user_id'] == session['user_id']
        if( not is_owner and journey['status'] == 'private'):
            return render_template('access_denied.html'), 403
        else:
            title = journey['journey_title']
            description = journey['journey_description']
            start_date = journey['start_date']
            journey_status=journey['status']
            return render_template('journey_details.html',
                                is_owner=is_owner,
                                journey_title=title,
                                journey_description=description,
                                journey_start_date=start_date,
                                journey_id=journey_id,
                                journey_status=journey_status,
                                events=events)
    else:
        journey_description_error = None
        journey_title_error = None
        journey_start_date_error = None
    
        if request.method == 'POST':
            # update journey details
            title = request.form['journey_title']
            description = request.form['journey_description']
            start_date = request.form['journey_start_date']
            journey_status = request.form['journey_status']
            
            if not title:
                journey_title_error = 'Please enter journey title.'
            # less than 255 characters
            elif len(title) > 255:
                journey_title_error = 'Title is too long. Please enter a title with less than 255 characters.'
            
            if not description:
                journey_description_error = 'Please enter journey description.'
                
            if not start_date:
                journey_start_date_error = 'Please enter start date.'
            else:
                try:
                    parsed_date = datetime.strptime(start_date, '%Y-%m-%d')
                    # check if the start date is 100 years ago or 10 years in the future
                    if parsed_date < datetime.now() - timedelta(days=36500) or parsed_date > datetime.now() + timedelta(days=3650):
                        journey_start_date_error = 'Please enter a valid start date. It should be within 100 years ago or 10 years in the future.'
                except ValueError:
                    journey_start_date_error = 'Invalid date format. Please use DD-MM-YYYY.'
            if journey_description_error or journey_title_error or journey_start_date_error:
                return render_template(
                    'journey_details.html',
                    journey_description=description,
                    journey_title=title,
                    journey_start_date=start_date,
                    journey_description_error=journey_description_error,
                    journey_title_error=journey_title_error,
                    journey_start_date_error=journey_start_date_error,
                    journey_id = journey_id
                )
            else:
                with db.get_cursor() as cursor:
                    cursor.execute('UPDATE journeys SET journey_title = %s, journey_description = %s, start_date= %s, status=%s WHERE journey_id = %s',
                                (title, description,start_date, journey_status, journey_id))
                    flash('Journey updated successfully!', 'success')
                    
                    return redirect(url_for('journey_details',
                                            journey_description=description,
                                            journey_title=title,
                                            journey_start_date=start_date,
                                            journey_status=journey_status,
                                            journey_id=journey_id
                                        ))           
        if isinstance(journey['start_date'], datetime):
            journey['start_date'] = journey['start_date'].strftime('%Y-%m-%d')
        return render_template('journey_details.html', journey=journey)


@app.route('/journey_details/<int:journey_id>/delete', methods=['POST'])
def delete_journey(journey_id):
    """
    Delete the entire journey
    """

    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    #delete events associated with this journey
    with db.get_cursor() as cursor:
        cursor.execute(''' DELETE FROM events 
                       WHERE journey_id = %s''', (journey_id,))

    #delete the journey
    with db.get_cursor() as cursor:
        cursor.execute('''DELETE FROM journeys 
                        WHERE journey_id = %s''', (journey_id,) )
    
    flash('Journey has been deleted!', 'success')
    return redirect(url_for('my_journeys'))


# Salvo 
@app.route('/admin/edit_journey/<int:journey_id>', methods=['GET', 'POST'])
def admin_edit_journey(journey_id):
    """Placeholder for admin journey editing functionality"""
    pass

@app.route('/admin/edit_event/<int:event_id>', methods=['GET', 'POST'])
def admin_edit_event(event_id):
    """Placeholder for admin event editing functionality"""
    pass

@app.route('/admin/delete_event_photo/<int:event_id>', methods=['POST'])
def admin_delete_event_photo(event_id):
    """Placeholder for admin photo deletion functionality"""
    pass