# journeys_feed.py
from tapp import app, db
from flask import redirect, render_template, session, url_for

@app.route('/journeys_feed')
def journeys_feed():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    # Get user_id from session
    current_user_id = session.get('user_id')  
    
    query = """
                SELECT 
                    j.journey_id,
                    j.user_id,
                    u.username,
                    u.profile_image,
                    j.journey_title,
                    j.journey_description,
                    j.start_date AS journey_start_date,
                    j.status AS journey_status,
                    e.event_id,
                    e.event_title,
                    e.event_description,
                    e.start_date AS event_start_date,
                    e.event_location,
                    e.event_image
                FROM 
                    journeys j
                JOIN 
                    users u ON j.user_id = u.user_id
                LEFT JOIN
                    events e ON j.journey_id = e.journey_id
                WHERE 
                    j.status = 'public'
                    OR j.user_id = %(current_user_id)s  <!-- Show private journeys to owner -->
                ORDER BY
                    j.journey_id, e.event_id
                ;

            """
    with db.get_cursor() as cursor:
        cursor.execute(query, {'current_user_id': current_user_id})  # Pass user_id session['user_id'
        rows = cursor.fetchall() # Retrieves all results as a list of dictionaries (the cursor is configured in db.py to return dicts).

    # Group events by journey_id/journey_title
    journeys_feed = {}
    for row in rows:
        journey_id = row['journey_id']
        
        if journey_id not in journeys_feed:
            journeys_feed[journey_id] = {
                'id': journey_id,
                'user': {
                    'id': row['user_id'],
                    'name': row['username'],
                    'avatar': row['profile_image']
                },
                'title': row['journey_title'],
                'description': row['journey_description'],
                'start_date': row['journey_start_date'],
                'status': row['journey_status'],
                'events': []
            }
        
        if row['event_id']:  # If event exists
            journeys_feed[journey_id]['events'].append({
                'id': row['event_id'],
                'title': row['event_title'],
                'description': row['event_description'],
                'start_date': row['event_start_date'],
                'location': row['event_location'],
                'image': row['event_image']
            })
    print("Sample journey data:", list(journeys_feed.values())[0] if journeys_feed else "NO JOURNEYS FOUND")
    return render_template('journeys_feed.html', journeys_feed=list(journeys_feed.values())) # convert to lists so that Jinja can loop over
    