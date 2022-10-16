from calendar import Calendar
from src.MVC import controller
from src.MVC.models import db
from src.MVC.models.Model import EventCalendar, Event, User
from src.MVC.controller.BotController import BotController


class MySqlDriver:
    def __init__(self,controller:BotController,) -> None:
        self.controller = controller

        pass

    def _create_calendar(self, **args):
        """
        args(calendar_id = room_id)
        """
        try:
            calendar_id = args["calendar_id"]
            calendar = EventCalendar(id=calendar_id)
            db.session.add(calendar)
            db.session.commit()
        except:
            pass

        pass

    def _update_calendar(self, **args):
        """
        args = (id=line_room_id 必須　priod,name,month,)
        """
        name = ''
        value = None
        try:
            calendar_id = args['id']
            calendar = EventCalendar.query.get(calendar_id)

        except:
            pass
        try:
            if 'name' in args:
                name = 'name'
                value = args['name']
            elif 'month' in args:
                name = 'month'
                value = args['month']
            elif 'deadline' in args:
                name = 'deadline'
                value = args['deadline']
        except:
            pass

        if value:
            setattr(calendar,name,value)
            db.session.commit()

    pass

    def _get_calendar(self, **args):
        """
        args(id=line_room_id)
        """

        try:
            calendar_id = args['id']
            calendar = EventCalendar.query.get(calendar_id)
            return calendar
        except:
            return None


    
            




