from calendar import calendar
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import string
from src.MVC.models import db
from src.MVC.models.Model import EventCalendar, Event, User, Days
calendar_init_value = {
    'event_name': '',
    'deadline': datetime(year=2000,month=1,day=1,hour=0,minute=0,second=0),
    'month': 0,
}
class MySqlDriver:
    def __init__(self,controller="",group_id="") -> None:
        """
        LINEのグループIDと BotControllerが必要。
        args = (controller,group_id)
        """
        self.controller = controller
        self.group_id = group_id
        pass
    
    def _create_calendar(self, **args):
        """
        カレンダーの作成
        args(calendar_id = group_id)
        """

        calendar_id = args["calendar_id"]
        if not self._check_event_start(group_id=calendar_id):
            calendar = EventCalendar(group_id=calendar_id,**calendar_init_value)
            db.session.add(calendar)
            db.session.commit()
            db.session.close()
        pass

    def _check_event_start(self, group_id):
        """
        カレンダーの要素を変更できるかどうかの判定
        (group_id = group_id)
        """
        flag = False
        calendar = self._get_calendar(group_id=group_id)
        if calendar and calendar.is_update == 1:
            flag = True
        return flag
    

    def _end_of_the_update_calendar(self,group_id):
        """
        カレンダーの要素を変更できなくする
        (group_id = group_id)
        """
        calendar = self._get_calendar(group_id=group_id)
        calendar.is_update = 0
        db.session.add(calendar)
        db.session.commit()
        db.session.close()
        
    def _update_calendar(self, **args):
        """
        カレンダーの要素の変更
        args = (group_id=line_room_id 必須　deadline,event_name,month,)
        """
        name = ''
        value = None
        if 'group_id' in args:
            calendar_id = args['group_id']
        
        calendar = self._get_calendar(group_id=calendar_id)
        print(calendar,flush=True)
        if 'month' in args:
            name = 'month'
            value = args['month']
            calendar.month = value
            print(value,flush=True)
        elif 'deadline' in args :
            name = 'deadline'
            value = datetime.today()+timedelta(int(args['deadline']))
            calendar.deadline = value
            print(value,flush=True)
        elif 'event_name' in args:
            name = 'event_name'
            value = args['event_name']
            calendar.event_name = value
            print(value,flush=True)
        

        print(calendar.to_dict(),flush=True)
        db.session.add(calendar)
        db.session.commit()
        db.session.close()
        
        return True
    pass

    def _get_calendar(self, **args):
        """

        args(group_id=line_room_id)
        """
        calendar_id = args['group_id']
    
        calendar = db.session.query(EventCalendar).get(calendar_id)
        #calendar = EventCalendar.query.get(calendar_id)
        db.session.close()
        return calendar
    
    def _delete_calendar(self, **args):
        if 'group_id' in args:
            calendar_id = args['group_id']
        
            calendar = self._get_calendar(group_id=calendar_id)
            db.session.delete(calendar)
            db.session.commit()
            db.session.close()

    def _register_event(self, **args):
        """
        'group_id': 
        'date': 
        'calendar_id': 
        'name': 
        'start_time': 
        'end_time': 
        """

        event = Event(**args)
        db.session.add(event)
        db.session.commit()
        db.session.close()
        return True
        
        pass

    def _search_events(self, group_id:string):
        """
        グループIDと一致するイベントを入手
        args=(group_id)
        """

        events = Event.query.where(Event.calendar_id==group_id)
        db.session.close()
        return events



    def _delete_event(self, **args):
        """

        args = (group_id = group_id)
        """
        events = Event.query.filter(Event.calendar_id==args["group_id"]).all()
        for e in events:
            db.session.delete(e)
        db.session.commit()
        db.session.close()
        
        pass

    def _vote_event(self, **args):
        """
        イベントの投票処理を行う
        args = (flag:boolean,group_id=number)
        """
        event_id = args['event_id']
        user_id = args['user_id']
        vote = args['vote']
        with db.session.connection():
            event:Event = Event.query.get(event_id)
            if vote == 'up':
                event.vote_num+=1
                event.voted_people+="{},".format(user_id)
            else:
                event.vote_num-=1
                voted_people = ''
                for people in event.voted_people.split(","):
                    if (user_id != people):voted_people+=people+","
                event.voted_people=voted_people
            db.session.add(event)
            db.session.commit()
        db.session.close()
        pass

    def _get_user(self, **args):
        """
        group_id
        """    
        user = User.query.get(args['group_id'])
        db.session.close()
        return user
       


    def _create_user(self):
        user = User()
        db.session.add(user)
        db.session.commit()
        db.session.close()
    def _register_user(self, **args):
        """
        name 
        event_calendar_id
        """
        group_id= args['event_calendar_id']+':'+args['name']
        user = User(group_id,**args)
        db.session.add(user)
        db.session.commit()
        db.session.close

        pass

    def _get_voted_event(self,**args):
        """
        得票数が１以上のイベントを入手
        args = (group_id)
        """
        group_id = args['group_id']
        events = Event.query.filter(Event.vote_num>0,Event.calendar_id==group_id).\
            order_by(Event.vote_num.desc()).\
            all()
        
        return events 

        pass
    def _register_days(self,args):
        h = 9
        add_list = []
        args = args['data']
        i = 0
        print(args,flush=True)
        for hour in range(len(args)//2):
            for time in range(2):
                day =  Days(h,30*time,args[i])
                add_list.append(day)
                i+=1
            h+=1
            print(h)

        db.session.add_all(add_list)
        db.session.commit()
        db.session.close()



    def _get_days(self,args):
        days = Days.query.all()
        days = [d.to_dict() for d in days]

        return days
        

    


        
        
        
        


    
            




