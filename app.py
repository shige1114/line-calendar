
from flask import Flask, request, abort, session
from flask_migrate import Migrate
from src.MVC.models import db
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

from src.MVC.controller.BotController import BotController
from datetime import timedelta

app = Flask(__name__,instance_relative_config=False)
app.config.from_pyfile('config.py')
db.init_app(app)
Migrate(app,db)
#環境変数取得
MY_CHANNEL_ACCESS_TOKEN = os.environ["MY_CHANNEL_ACCESS_TOKEN"]
MY_CHANNEL_SECRET = os.environ["MY_CHANNEL_SECRET"]

line_bot_api = LineBotApi(MY_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(MY_CHANNEL_SECRET)


#

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
		
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


"""
help message
"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    bot_controller = BotController(line_bot_api=line_bot_api,session=session)
    id,value = bot_controller._bot_controller(event=event)
    
        
    

if __name__ == "__main__":
    app.run()
