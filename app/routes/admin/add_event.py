from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from app.models.admin import Event

@app.route('/add_event', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        event_date = datetime.strptime(request.form.get('event_date'), '%Y-%m-%d')
        event_venue = request.form.get('event_venue')
        eligibility = request.form.get('eligibility')
        total_tickets = int(request.form.get('total_tickets'))

        #check if an event already exists

        exisiting_event = Event.query.first()

        if exisiting_event:
            #override exisiting details with new details
            exisiting_event.event_name = event_name
            exisiting_event.event_date = event_date
            exisiting_event.event_venue = event_venue
            exisiting_event.eligibility = eligibility
            exisiting_event.total_tickets = total_tickets
        else:
            #create a new event to the db
            new_event = Event(
                event_name=event_name,
                event_date=event_date,
                event_venue=event_venue,
                eligibility=eligibility,
                total_tickets=total_tickets
            )

            db.session.add(new_event)
            db.session.commit()
            flash('New Event Added Succesfully.', 'success')
            return redirect(url_for('dashboard'))


    return render_template('admin/add_event.html')