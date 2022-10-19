

class View:

    def __init__(self,controller=None) -> None:
        self.controller = controller
        pass

    def _start_event_message(self,):
        return "!eventと打ってみてください。"
        pass
    
    def _select_month_masssage(self,):
        return "何月に遊びますか？"
        pass

    def _decide_priod_massage(self, message=""):
        return "投票期間を決めてください！"
        pass

    def _decide_event_name(self,):
        return "名前を決めてください！"

    def _sent_url_massage(self, message=""):
        return """
        イベント候補を登録してください！
        https://gesh-calendar-1114.vercel.app/event_view?room_id={}
        """.format(self.controller.room_id)
        pass

    def _announcement_result_massage(self, message=""):
        return "結果はっぴょー！！"
        pass

    def _error_message(self, message=""):
        return "error"
        pass
    def _default_card():

        pass
