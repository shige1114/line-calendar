
from email import message
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from src.MVC.view.View import View
from flask_session import Session
import typing as tp
from flask import session
if tp.TYPE_CHECKING:
    from flask import session


class BotController:
    def __init__(self, line_bot_api, session: "session") -> None:

        try:
            self.line_bot_api = line_bot_api
            self.session = session
            self.view = View()
        except:
            print("!error message i couldnt read line_bot_api!")

    def _bot_controller(self, event=""):
        message = event.message.text
        if "!event" == message:
            self._start_event(event)
            return ["login", True]
        elif not self.session.get("login"):
            return [None,None]
        elif self._check_month(event):
            self._select_month(event)
            return ["month", self._select_month(event)]
        elif self._check_priod_message(event):
            self._decide_event_name(self, event)
            return ["priod", self._check_month(event)]
            pass
        elif self.session.get('login'):
            self._decide_event_name(event)
            return ["name", event.message.text]
        
        return [None, None]

        pass

    def _start_event(self, event):
        self._send_message(
            event,
            message=self.view._select_month_masssage()
        )
        self._send_message(
            event,
            message=self.view._error_message()
        )

        pass

    def _select_month(self, event):
        if self.session.get("login") == "True":
            self._send_message(
                event,
                message=self.view._decide_priod_massage()
            )

        else:
            self._send_message(
                event,
                message=self.view._error_message()
            )

        pass

    def _decide_event_name(self, event):
        self._send_message(event, self.view._sent_url_massage())

        pass

    def _decide_priod(self, message=""):
        pass

    def _sent_url(self, message=""):
        pass

    def _announcement_result(self, message=""):
        pass

    def _error_message(self, event):
        self._send_message(
            event,
            message=self.view._error_message()
        )
        pass

    def _send_message(self, event="", message=""):
        self.line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
        pass

    """
    イベント型を入れてください。
    """

    def _check_month(self, event=""):
        message = event.message.text
        month = None
        if '月' in message:
            month = message.split("月")
            return int(month[0])
        else:
            return month
        pass

    def _check_priod_message(self, event=""):
        message = event.message.text
        priod = None
        if '日' in message:
            priod = message.split("日")
            return int(priod[0])
        else:
            return priod
    