from datetime import datetime

from sqlalchemy import ForeignKey
from src.MVC.models import db

class EventCalendar(db.Model):
    """
    EventCalendar(id=line_room_id,**args)
    """
    __tablename__ = 'EventCalendar'

    id = db.Column(db.String(255), primary_key=True,)
    event_name = db.Column(db.String(255), nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    month = db.Column(db.String(255), nullable=True)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    def __init__(self,id, event_name, priod, month):
        self.id = id
        self.event_name = event_name
        self.priod = priod
        self.month = month

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'event_name': self.event_name,
            'priod': self.priod,
            'month': self.month,
            'created_date': self.created_date,
            'updated_date' : self.updated_date,
        }

class User(db.Model):
    """
    User(id=line_id)
    """
    __tablename__ = 'User'

    id = db.Column(db.String(255), primary_key=True,)
    name = db.Column(db.String(255), nullable=False)
    event_calendar_id = db.Column(db.String(255), nullable=False)
    voted_event = db.Column(db.String(255), nullable=False)
    voted_number = db.Column(db.Integer,default=0, nullable=False)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,id, name, event_calendar_id, voted_event):
        self.id = id
        self.name = name
        self.event_calendar_id = event_calendar_id
        self.voted_event = voted_event

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'name': self.name,
            'event_calendar_id': self.event_calendar_id,
            'voted_event': self.voted_event,
            'created_date': self.created_date
        }


class Event(db.Model):
    """Event
    """
    __tablename__ = 'Event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(255), nullable=False)
    calendar_id = db.Column(db.String(255),ForeignKey("EventCalendar.id"),nullable=False)
    name = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.Time, nullable=False,)
    end_time = db.Column(db.Time, nullable=False,)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, date, name, detail,start_time,end_time,calendar_id):
        self.date = date
        self.name = name
        self.detail = detail
        self.start_time=start_time
        self.end_time=end_time
        self.calendar_id=calendar_id

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'date': self.date,
            'calendar_id':self.calendar_id,
            'name': self.name,
            'detail': self.detail,
            'start_time' : self.start_time,
            'end_time': self.end_time,
            'created_date': self.created_date
        }
