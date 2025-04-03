from journeyapp import app
from journeyapp import db
from flask import redirect, render_template, request, session, url_for,flash
from datetime import datetime, timedelta

@app.route('/journey_details/<int:journey_id>/add_event', methods=['GET', 'POST'])
def add_event(journey_id):
    if 'loggedin' not in session:
         return redirect(url_for('login'))
    
    with db.get_cursor() as cursor:
        cursor.execute('SELECT journey_id, journey_title FROM journeys WHERE journey_id = %s;', (journey_id,))
        journey = cursor.fetchone()

    if request.method == 'POST' and 'event_title' in request.form and 'event_description' in request.form and 'event_start_date' in request.form and 'event_location' in request.form:
        title = request.form['event_title']
        description = request.form['event_description']
        start_date = request.form['event_start_date']
        end_date = request.form['event_end_date']
        location = request.form['event_location']

        event_title_error = None
        event_description_error = None
        event_start_date_error = None
        event_end_date_error = None
        event_location_error = None

        if not title:
            event_title_error = 'Event title is required.'
        elif len(title) > 100:
            event_title_error = 'Event title cannot exceed 100 characters.'

        if description:
            if len(description) > 300:
                event_description_error = 'Event description cannot exceed 300 characters.'

        if not start_date:
            event_start_date_error = 'Event start date is requried.'
        else:
            try:
                parsed_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
                # check if the start date is 100 years ago or 10 years in the future
                if parsed_date < datetime.now() - timedelta(days=36500) or parsed_date > datetime.now() + timedelta(days=3650):
                    event_start_date_error = 'Please enter a valid start date. It should be within 100 years ago or 10 years in the future.'
            except ValueError:
                event_start_date_error = 'Invalid date format. Please use DD-MM-YYYY.'

        if end_date:
            try:
                parsed_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
                # check if the end date is 100 years ago or 10 years in the future
                if parsed_date < datetime.now() - timedelta(days=36500) or parsed_date > datetime.now() + timedelta(days=3650):
                    event_end_date_error = 'Please enter a valid end date. It should be within 100 years ago or 10 years in the future.'
            except ValueError:
                event_end_date_error = 'Invalid date format. Please use DD-MM-YYYY.'

        if not location:
            event_location_error = 'Event location is required.'
        elif len(location) > 50:
            event_location_error = 'Event location cannot exceed 50 characters.'

        if event_title_error or event_description_error or event_start_date_error or event_end_date_error or event_location_error:
            return render_template(
                'add_event.html', 
                journey=journey, 
                event_title=title,
                event_description=description,
                event_start_date=start_date,
                event_end_date=end_date,
                event_location=location,
                event_title_error=event_title_error, 
                event_description_error=event_description_error, 
                event_start_date_error=event_start_date_error, 
                event_end_date_error=event_end_date_error, 
                event_location_error=event_location_error)
        else:
            with db.get_cursor() as cursor:
                cursor.execute('''INSERT INTO events (journey_id, event_title, event_description, start_date, end_date, event_location) 
                               VALUES (%s, %s, %s, %s, %s, %s);''', 
                               (journey_id, title, description or None, start_date, end_date or None, location))
                flash('Event added successfully!', 'success')
            return redirect(url_for('add_event', journey_id=journey_id))
    return render_template('add_event.html', journey=journey)