
from shutil import ExecError
from linebot.exceptions import (
    InvalidSignatureError,
)
from linebot import (
    LineBotApi,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from src.MVC.models.Model import EventCalendar
from src.MVC.view.View import View
from src.MVC.models.MySqlDriver import MySqlDriver


class BotController:
    def __init__(self, line_bot_api: LineBotApi, event: MessageEvent) -> None:

        try:
            self.line_bot_api = line_bot_api
            self.event = event
            self.room_id = event.source.group_id
            self.name = line_bot_api.get_profile(event.source.user_id)
            self.text = event.message.text
            self.models = MySqlDriver(line_bot_api, self.room_id)
            self.view = View(self)
        except Exception as e:
            print(e, flush=True)

    def _bot_controller(self, ):
        event = self.event
        if "!event" == self.text:
            self._start_event(event)
            pass
        elif "!finish" == self.text:
            self._inform_vote_result(event)
            pass
        elif self.models._check_event_start(id=self.room_id):
            self._select_month(event)
            self._decide_deadline(event)
            self._decide_event_name(event)
        
            pass


        pass

    def _start_event(self, event):

        self.models._create_calendar(calendar_id=self.room_id)
        self._send_message(
            self.event,
            message=self.view._select_month_masssage()
        )
        pass

    def _select_month(self, event):
        if self._check_month(self.event):
            self.models._update_calendar(
                id=self.room_id, month=self._check_month(self.event)
            )
            self._send_message(
                self.event,
                message=self.view._decide_deadline_massage()
            )

        pass

    def _decide_event_name(self, event):
        if not (self._check_deadline_message(self.event) or self._check_month(self.event)):
            self.models._update_calendar(
                id=self.room_id, event_name=self.event.message.text
            )
            self._send_message(
                self.event,
                self.view._sent_url_massage()
            )
            self.models._end_of_the_update_calendar(id=self.room_id)

        pass

    def _decide_deadline(self, message=""):
        if self._check_deadline_message():
            self.models._update_calendar(
                id=self.room_id, deadline=self._check_deadline_message()
            )
            self._send_message(
                self.event,
                self.view._decide_event_name()
            )
        pass

    def _error_message(self, event=""):
        self._send_message(
            self.event,
            message=self.view._error_message()
        )
        pass

    def _send_message(self, event="", message=""):
        try:
            self.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=message)
            )
        except(Exception):
            print(Exception)

    def _check_month(self, event=""):
        month = None
        if '月' in self.text:
            month = self.text.split("月")
            return int(month[0])
        else:
            return month
        pass

    def _check_deadline_message(self, event=""):

        deadline = None
        if '日' in self.text:
            deadline = self.text.split("日")
            return int(deadline[0])
        else:
            return deadline

    def _inform_vote_result(self, event=""):
        events = self.models._get_voted_event(room_id=self.room_id)
        self._send_message(
            self.event,
            self.view._inform_vote_result(events)
        )
        self.models._delete_calendar(id=self.room_id)
        
