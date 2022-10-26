
from calendar import month
from flask import Flask, request, abort, session
from flask_cors import CORS
from flask_migrate import Migrate
from src.MVC.models import db
from src.MVC.view.WebVeiw import WebView
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
from src.MVC.models.MySqlDriver import MySqlDriver
from datetime import datetime

app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')
app.register_blueprint(WebView)
db.init_app(app)
Migrate(app,db)
CORS(app,resources={r'/*' : {'origins':['https://gesh-cal.vercel.app',"https://liff.line.me/1657580536-VQdodb56"]}})

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
    body = request.get_data(as_text=False)
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
    
    bot_controller = BotController(line_bot_api=line_bot_api,event=event)
    bot_controller._bot_controller(event=event)
    
        
    

if __name__ == "__main__":
    app.run()
