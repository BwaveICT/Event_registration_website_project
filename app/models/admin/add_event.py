from datetime import datetime
from app import db 

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    event_name = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    event_venue = db.Column(db.String(100), nullable=False)
    eligibility = db.Column(db.String(100), nullable=False)
    total_tickets = db.Column(db.Integer, nullable=False)