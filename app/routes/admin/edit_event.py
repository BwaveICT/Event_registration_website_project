from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.admin import Event

@app.route('/edit_event', methods=['GET', 'POST'])
@login_required
def edit_event():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        event_date = request.form.get('event_date')
        event_venue = request.form.get('event_venue')
        eligibility = request.form.get('eligibility')
        total_tickets = int(request.form.get('total_tickets'))


        event_id = request.args.get('event_id')

        existing_event = Event.query.get(event_id)

        if existing_event:
            #update exisiting event
            existing_event.event_name = event_name
            existing_event.event_date = event_date
            existing_event.event_venue = event_venue
            existing_event.eligibility = eligibility
            existing_event.total_tickets = total_tickets

            db.session.commit()
            flash('Event details edited successfully', 'success')
            return redirect(url_for('dashboard'))


    event_id = request.args.get('event_id')

    existing_event = Event.query.get(event_id)

    if existing_event:
        return render_template('admin/edit_event.html', existing_event=existing_event)
    else:
        flash('Event not found', 'danger')
        return redirect(url_for('dashboard')) 