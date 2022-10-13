from email import message
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from src.MVC.view.View import View
import typing as tp


class BotController:
    def __init__(self, line_bot_api, session) -> None:

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
        elif self._check_month(event):
            self._select_month(event)
        elif "" == message:
            pass
        pass

    def _start_event(self, event):
        self.session.permanent = True
        self.session["start_event"] = True
        self._send_message(
            event,
            message=self.view._select_month_masssage()
        )
        pass

    def _select_month(self, event):
        if "start_event" in self.session:
            self.session["month"] = self._check_month(event.message.text)
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

        pass

    def _decide_priod(self, message=""):
        pass

    def _sent_url(self, message=""):
        pass

    def _announcement_result(self, message=""):
        pass

    def _error_message(self, message=""):
        pass

    def _send_message(self, event="", message=""):
        self.line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
        pass

    def _check_month(self, message=""):
        month = None
        if '月' in message:
            month = message.split("月")
            return int(month)
        else:
            return month
        pass
