
from shutil import ExecError
from linebot.exceptions import (
    InvalidSignatureError,
)
from linebot import (
    LineBotApi,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
from src.MVC.models.Model import EventCalendar
from src.MVC.view.View import View
from src.MVC.models.MySqlDriver import MySqlDriver


class BotController:
    def __init__(self, line_bot_api: LineBotApi, event: MessageEvent) -> None:
        """
        LineBotApi
        event
        """
        self.line_bot_api = line_bot_api
        self.event = event
        try:
            self.group_id = event.source.group_id
        except Exception:
            self.group_id = None
        self.name = line_bot_api.get_profile(event.source.user_id)
        self.text = event.message.text
        self.models = MySqlDriver(line_bot_api, self.group_id)
        self.view = View(self)


    def _bot_controller(self, ):
        """
        入力されたテキスト処理
        """
        event = self.event
        if "!event" == self.text:
            self._start_event(event)
            pass
        elif "!finish" == self.text:
            self._inform_vote_result(event)
            pass
        elif "会議したいです" == self.text:
            self._test_bot(event)

        elif "送信しました" == self.text:
            self._flex_bot(event)
        elif self.models._check_event_start(group_id=self.group_id):
            self._select_month(event)
            self._decide_deadline(event)
            self._decide_event_name(event)

            pass

        pass

    def _flex_bot(self, event):
        payload = {
  "type": "flex",
  "altText":"this is flex",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": " 3 月 9 日 11:00~12:00",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "会議予定時刻"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "承認",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "却下",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": " 3 月 9 日 13:00~",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "会議予定時刻"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "承認",
              "uri": "http://linecorp.com/"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "却下",
              "uri": "http://linecorp.com/"
            }
          }
        ]
      }
    }
  ]
}

        flex_message = FlexSendMessage(contents=payload)
        self.line_bot_api.reply_message(
                self.event.reply_token,
                flex_message
            )

    def _test_bot(self, event):
        self._send_message(
            self.event,
            message="""わかりました。
会議に最適な時間を予測します。
こちらが空き時間の予測結果です。
https://liff.line.me/1657580536-XNyMy30d
            """
        )

    def _start_event(self, event):
        """
        最初の処理、
        カレンダーを制作後、月を選択させるメッセージを送る
        """
        self.models._create_calendar(calendar_id=self.group_id)
        self._send_message(
            self.event,
            message=self.view._select_month_masssage()
        )
        pass

    def _select_month(self, event):
        """
        カレンダーの月を更新後、投票締切日を入力させるメッセージを送る
        """
        if self._check_month(self.event):
            self.models._update_calendar(
                group_id=self.group_id, month=self._check_month(self.event)
            )
            self._send_message(
                self.event,
                message=self.view._decide_deadline_massage()
            )

        pass

    def _decide_event_name(self, event):
        """
        １、カレンダーの名前を入力する。
        ２、LiffのURLを送る。
        ３、カレンダーの要素を変更不可に
        """
        if not (self._check_deadline_message(self.event) or self._check_month(self.event)):
            self.models._update_calendar(
                group_id=self.group_id, event_name=self.event.message.text
            )
            self._send_message(
                self.event,
                self.view._sent_url_massage()
            )
            self.models._end_of_the_update_calendar(group_id=self.group_id)

        pass

    def _decide_deadline(self, message=""):
        """
        １、カレンダーの要素の締切日を決める。
        ２、名前を決めるメッセージを送る。
        """
        if self._check_deadline_message():
            self.models._update_calendar(
                group_id=self.group_id, deadline=self._check_deadline_message()
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
        """
        Lineでグループにメッセージを送る
        """
        try:
            self.line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=message)
            )
        except (Exception):
            print(Exception)

    def _check_month(self, event=""):
        """
        カレンダーの要素である何月含むメッセージかどうか判定
        """
        month = None
        if '月' in self.text:
            month = self.text.split("月")
            return int(month[0])
        else:
            return month
        pass

    def _check_deadline_message(self, event=""):
        """
        締切日を含むメッセージかどうか判定
        """
        deadline = None
        if '日' in self.text:
            deadline = self.text.split("日")
            return int(deadline[0])
        else:
            return deadline

    def _inform_vote_result(self, event=""):
        """
        !finishを入力された際に、投票結果のメッセージを送る。
        """
        events = self.models._get_voted_event(group_id=self.group_id)
        self._send_message(
            self.event,
            self.view._inform_vote_result(events)
        )
        self.models._delete_event(group_id=self.group_id)
        self.models._delete_calendar(group_id=self.group_id)
