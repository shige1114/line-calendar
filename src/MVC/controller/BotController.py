from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from requests import session
from sqlalchemy import true
from ..view.View import View
import typing as tp


class BotController:
    def __init__(self,line_bot_api) -> None:
        self.view = View()
        try:
            self.line_bot_api = line_bot_api
            #self.session = args["session"]
        except:
            print("!error message i couldnt read line_bot_api!")

    def _bot_controller(self, event=""):
        message = event.message.text
        if "!event" == message and not self.session["start_event"]:
            self._start_event(event)
        elif self._check_month():
            self._select_month(event)
        elif "" == message:
            pass
        pass

    def _start_event(self, event):
        #self.session.permanent = True
        #self.session["start_event"] = True
        self.line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="イベント開催月を決定してください。")
        )
        pass



    def _select_month(self, event):
        #if self.session["start_event"]:
            #self.session["month"] = self._check_month(event.message.text)
            #self.line_bot_api.reply_message(
            #    event.reply_token,
            #    TextSendMessage(text="イベントの名前を入力してください。")
            #)

        pass

    def _decide_event_name(self,event):

        pass
    def _decide_priod(self, message=""):
        pass

    def _sent_url(self, message=""):
        pass

    def _announcement_result(self, message=""):
        pass

    def _error_message(self, message=""):
        pass

    def _check_month(self, message=""):
        month = None
        if '月' in message:
            month = message.split("月")
            return int(month)
        else:
            return month
        pass
