from datetime import date, datetime
from email.policy import default

from sqlalchemy import ForeignKey, Integer
from src.MVC.models import db


class EventCalendar(db.Model):
    """
    EventCalendar(id=line_room_id,**args)
    """
    __tablename__ = 'event_calendar'

    id = db.Column(db.String(255), primary_key=True,)
    event_name = db.Column(db.String(255), nullable=True, default="")
    deadline = db.Column(db.DateTime, nullable=True,
                         default=datetime.today())
    is_update = db.Column(db.Integer(),nullable=True,
                         default=1)
    month = db.Column(db.Integer(), nullable=True, default=0)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.today())
    updated_date = db.Column(
        db.DateTime, nullable=False, default=datetime.today()
    )

    def __init__(self, id, event_name, deadline, month,is_update=1):
        self.id = id
        self.event_name = event_name
        self.deadline = deadline
        self.month = month
        self.is_update = is_update

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'event_name': self.event_name,
            'deadline': self.deadline,
            'month': self.month,
            'created_date': self.created_date,#.strftime("%Y-%m-%d"),
            'updated_date': self.updated_date,#.strftime("%Y-%m-%d"),
        }


class User(db.Model):
    """
    User(id=line_id)
    """
    __tablename__ = 'user'

    id = db.Column(db.String(255), primary_key=True,)
    name = db.Column(db.String(255), nullable=False)
    event_calendar_id = db.Column(db.String(255), ForeignKey(
        "event_calendar.id"), nullable=False)
    voted_event = db.Column(db.String(255), nullable=False)
    voted_number = db.Column(db.Integer(), default=0, nullable=False)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.today())

    def __init__(self, id='test', name='test', event_calendar_id='jfladjfa', voted_event=''):
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
            'created_date': self.created_date.strftime("%Y-%m-%d")
        }


class Event(db.Model):
    """Event
    """
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(255), nullable=False)
    calendar_id = db.Column(db.String(255), ForeignKey(
        "event_calendar.id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    vote_num = db.Column(db.Integer, nullable=False,)
    start_time = db.Column(db.String(255), nullable=False,)
    end_time = db.Column(db.String(255), nullable=False,)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.today())
    voted_people = db.Column(db.String(255), nullable=False,)

    def __init__(self, date, name,  start_time, end_time, calendar_id, vote_num=0,voted_people=""):
        self.date = date
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.calendar_id = calendar_id
        self.vote_num = vote_num
        self.voted_people = voted_people

    def to_dict(self):
        """to_dict
        """
        return {
            'id': self.id,
            'date': self.date,
            'calendar_id': self.calendar_id,
            'name': self.name,
            'vote_num': self.vote_num,
            'voted_people':self.voted_people,
            'start_time': self.start_time,#"{}:{}".format(self.start_time.hour,self.start_time.minute),
            'end_time': self.end_time,#"{}:{}".format(self.end_time.hour,self.end_time.minute),
            'created_date': self.created_date#.strftime("%Y-%m-%d")
        }

class Days(db.Model):
    __tablename__ = 'day'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hour =db.Column(db.Integer, nullable=False,) 
    minites = db.Column(db.Integer, nullable=False,)
    day_class = db.Column(db.Integer, nullable=False,)

    def __init__(self,hour,minites,day_class) -> None:
        super().__init__()

        self.hour = hour      
        self.minites = minites
        self.day_class = day_class

    def to_dict(self):

        return {
            "hour":self.hour,
            "minites":self.minites,
            "day_class":self.day_class
        }