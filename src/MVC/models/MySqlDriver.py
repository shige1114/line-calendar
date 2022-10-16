from calendar import month
from datetime import datetime, timedelta
from src.MVC.models import db
from src.MVC.models.Model import EventCalendar, Event, User

calendar_init_value = {
    'event_name': '',
    'priod': datetime.today(),
    'month': 0,
}
class MySqlDriver:
    def __init__(self,controller="",room_id="") -> None:
        self.controller = controller
        self.room_id = room_id
        pass

    def _create_calendar(self, **args):
        """
        args(calendar_id = room_id)
        """
        
        calendar_id = args["calendar_id"]
        calendar = EventCalendar(id=calendar_id,**calendar_init_value)
        
        db.session.add(calendar)
        db.session.commit()
        db.session.close()
        

        pass

    def _update_calendar(self, **args):
        """
        args = (id=line_room_id 必須　priod,name,month,)
        """
        name = ''
        value = None
        if 'id' in args:
            calendar_id = args['id']
        else:
            calendar_id = self.room_id
        calendar = EventCalendar.query.get(calendar_id)

        if 'event_name' in args:
            name = 'event_name'
            value = args['event_name']
        elif 'month' in args:
            name = 'month'
            value = args['month']
        elif 'priod' in args:
            name = 'priod'
            value = datetime.today() - timedelta(int(args['priod']))
        

        if value:
            setattr(calendar,name,value)
            db.session.commit()
            db.session.close()

    pass

    def _get_calendar(self, **args):
        """
        args(id=line_room_id)
        """
        if 'id' in args:
            calendar_id = args['id']
        else:
            calendar_id = self.room_id
        
        calendar_id = args['id']
        calendar = EventCalendar.query.get(calendar_id)
        db.session.close()
        return calendar
        
        
        


    
            




