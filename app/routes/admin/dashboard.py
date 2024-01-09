from flask import render_template
from app import app
from flask_login import login_required
from app.models.admin import Event
from app.models.user import Registration

@app.route('/dashboard')
@login_required
def dashboard():    
    # Retrieve existing_events from the database
    existing_event = Event.query.first()

    if existing_event:
        total_tickets = existing_event.total_tickets

        #count the number of registered users
        tickets_used = Registration.query.count()


        # calculate the number of tickets left
        tickets_left = total_tickets - tickets_used


        # Retrieve all user registrations
        registrations = Registration.query.all()


        return render_template(
            'admin/dashboard.html',
            total_tickets=total_tickets,
            tickets_used=tickets_used,
            tickets_left=tickets_left,
            existing_event=existing_event,
            registrations=registrations
        )

    return render_template('admin/dashboard.html')