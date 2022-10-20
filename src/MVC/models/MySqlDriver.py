from asyncio import events
from calendar import month
from datetime import datetime, timedelta
import string
from unicodedata import name
from src.MVC.models import db
from src.MVC.models.Model import EventCalendar, Event, User

calendar_init_value = {
    'event_name': '',
    'deadline': datetime(year=2000,month=1,day=1,hour=0,minute=0,second=0),
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

    def _check_event_start(self, id):
        """
        (id = group_id)
        """
        return EventCalendar.query.get(id)

    def _update_calendar(self, **args):
        """
        args = (id=line_room_id 必須　deadline,name,month,)
        """
        name = ''
        value = None
        if 'id' in args:
            calendar_id = args['id']
        else:
            calendar_id = self.room_id
        calendar = self._get_calendar(id=calendar_id)
        if 'month' in args:
            name = 'month'
            value = args['month']
        elif 'deadline' in args and  calendar.month != calendar_init_value['month']:
            name = 'deadline'
            value = datetime.today()+timedelta(int(args['deadline']))
        elif 'event_name' in args and calendar.deadline != calendar_init_value['deadline']:
            name = 'event_name'
            value = args['event_name']
        

        if value:
            setattr(calendar,name,value)
            db.session.commit()
            db.session.close()
        
        return True
    pass

    def _get_calendar(self, **args):
        """
        args(id=line_room_id)
        """
        if 'id' in args:
            calendar_id = args['id']
        else:
            calendar_id = self.room_id

        calendar = EventCalendar.query.get(calendar_id)
        db.session.close()
        return calendar
    
    def _delete_calendar(self, **args):
        if 'id' in args:
            calendar_id = args['id']
        else:
            calendar_id = self.room_id
        calendar = EventCalendar.query.get(calendar_id)
        db.session.delete(calendar)
        db.session.commit()
        db.session.close()

    def _register_event(self, **args):
        """
        'id': 
        'date': 
        'calendar_id': 
        'name': 
        'detail': 
        'start_time': 
        'end_time': 
        'created_date': 
        """
        event = Event(**args)
        db.session.add(event)
        db.session.commit()
        db.session.close()
        
        pass

    def _search_events(self, room_id:string):
        """
        args=(room_id)
        """

        events = Event.query.filter(room_id).all()
        return events



    def _delete_event(self, **args):
        """
        
        """
        
        pass

    def _vote_event(self, **args):
        """
        args = (flag:boolean,id=number)
        """
        flag = args['flag']
        with db.session.commit():
            event:Event = Event.query.get(args['id'])
            if flag:
                event.vote_num+=1
            else:
                event.vote_num-=1
            db.session.commit()
        db.session.close()
        pass
    def _get_user(self, **args):
        """
        room_id
        user.name
        """
        try:
            id = args["room_id"]+":"+args["name"]
            user = User.query.get(id)
            return user
        except Exception as e :
            print(e)



    def _register_user(self, **args):
        """
        name 
        event_calendar_id
        """
        id= args['event_calendar_id']+':'+args['name']
        user = User(id,**args)
        db.session.add(user)
        db.session.commit()
        db.session.close

        pass

    def _delete_user(self, **args):
        pass


        
        
        
        


    
            




