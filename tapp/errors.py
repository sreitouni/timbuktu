from tapp import app
from flask import render_template, session


# Error handlers :)                     ref : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses
@app.errorhandler(400)              
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(Exception)
def handle_errors(error):
    """Unified error handler for Flask"""
    
    error_map = {
        400: "400 Bad Request: Your request contains invalid data.",
        404: "Page not found",
        500: "An internal server error occurred.",
    }

    error_code = getattr(error, 'code', 500)  # Default to 500 if no specific error code exists
    error_message = error_map.get(error_code, "An unexpected error occurred.")

    # Select base template based if loggedin or not.
    base_template = "userbase.html" if session.get('loggedin') else "base_public.html"

    return render_template('error.html', error_code=error_code, error_message=error_message, base_template=base_template), error_code