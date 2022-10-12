from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from ..view.View import View


class BotController:
    def __init__(self, **args) -> None:
        self.view = View()
        try:

            self.line_api = args["line_api"]
        except:
            print("!error message i couldnt read line_api!")

    def _bot_controller(self, event=""):
        message = event.message.text
        if "!event" == message:
            self._start_event(event)
        elif "" == message:
            self._select_month()
        elif "" == message:
            pass
        pass

    def _start_event(self, event):
        
        self.line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="イベントの名前を入力してください。")
        )

        pass

    def _select_month(self, message=""):
        pass

    def _decide_priod(self, message=""):
        pass

    def _sent_url(self, message=""):
        pass

    def _announcement_result(self, message=""):
        pass
