from src.MVC.models.Model import (Event,EventCalendar)

class View:

    def __init__(self,controller=None) -> None:
        """
        LINEに送る文章の作成
        """
        self.controller = controller
        pass

    def _start_event_message(self,):
        return "!eventと打ってみてください。"
        pass
    
    def _select_month_masssage(self,):
        return "何月に遊びますか？"
        pass

    def _decide_deadline_massage(self, message=""):
        return "投票期間を決めてください！"
        pass

    def _decide_event_name(self,):
        return "名前を決めてください！"

    def _sent_url_massage(self, message=""):
        return """
https://liff.line.me/1657580536-VQdodb56
        """.format(self.controller.group_id)
        pass

    def _inform_vote_result(self, events=[]):
        text = "結果発表！！！"

        for i, event in enumerate(events):
            text += self._create_vote_result(i,event)

        return text

        pass
    def _create_vote_result(self,index,event:Event):
        """
        投票結果に関するテキストの追加
        """
        text = "\n・{}位\n日:{}\n時間:{}~{}\n参加者:{}".format(
            index+1,
            event.date,
            event.start_time,
            event.end_time,
            event.voted_people,
        )
        return text


    
    def _error_message(self, message=""):
        return "error"
        pass
    def _default_card():

        pass
