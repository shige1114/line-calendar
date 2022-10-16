
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot import (
    LineBotApi,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from src.MVC.view.View import View
from src.MVC.models.MySqlDriver import MySqlDriver


class BotController:
    def __init__(self, line_bot_api: LineBotApi, event: MessageEvent) -> None:

        try:
            self.line_bot_api = line_bot_api
            self.models = MySqlDriver(line_bot_api)
            self.view = View()
            self.event = event
            self.room_id = event.source.room_id
        except:
            print("!error message i couldnt read line_bot_api!")

    def _bot_controller(self, event: MessageEvent):

        message = event.message.text
        if "!event" == message:
            self._start_event(event)

            pass

        elif self._check_month(event):
            self._select_month(event)
            return ["month", self._select_month(event)]

            pass

        elif self._check_priod_message(event):
            self._decide_event_name(self, event)
            return ["priod", self._check_month(event)]

            pass
        elif self.models:
            self._decide_event_name(event)
            return ["name", event.message.text]

            pass
        return [None, None]

        pass

    def _start_event(self,event):
        self.models._create_calendar(calendar_id=self.room_id)
        self._send_message(
            self.event,
            message=self.view._select_month_masssage()
        )
        pass

    def _select_month(self, event):
        if self.models._get_calendar(self.room_id):
            self.models._update_calendar(
                id=self.room_id, monht=self._check_month()
            )
            self._send_message(
                self.event,
                message=self.view._decide_priod_massage()
            )

        pass

    def _decide_event_name(self, event):
        if self.models._get_calendar(self.room_id):
            self.models._update_calendar(
                id=self.room_id, name=self.event.message.text)
            self._send_message(
                self.event,
                self.view._sent_url_massage()
            )

        pass

    def _decide_priod(self, message=""):
        pass

    def _sent_url(self, message=""):
        pass

    def _announcement_result(self, message=""):
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
                self.event.reply_token,
                TextSendMessage(text=message)
            )
        except:
            print("error")
        pass

    def _check_month(self, event=""):
        message = self.event.message.text
        month = None
        if '月' in message:
            month = message.split("月")
            return int(month[0])
        else:
            return month
        pass

    def _check_priod_message(self, event=""):
        message = self.event.message.text
        priod = None
        if '日' in message:
            priod = message.split("日")
            return int(priod[0])
        else:
            return priod
