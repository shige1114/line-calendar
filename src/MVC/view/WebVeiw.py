from flask import Blueprint, jsonify, redirect, request, url_for
from src.MVC.controller.WebController import WebController
from src.MVC.models.MySqlDriver import MySqlDriver

WebView = Blueprint('webview',__name__,url_prefix='/webview')


@WebView.route('/', methods=['GET'])
def index():

    return '<h1>k<h1>'
@WebView.route('/login',methods=['GET'])
def login():

    pass
@WebView.route('/event_view', methods=['GET'])
def event_view():
    try:
        model = MySqlDriver()
        calendars=model._search_calendar(request.json["room_id"])
        
        
        return jsonify(calendars)
    except Exception as e:
        print(e)

    pass
@WebView.route('/user', methods=['POST'])
def user_register():
    try:
        data = request.json
        controller = WebController()
        controller._register_user(data)      
    except Exception as e:
        print(e)
    pass
@WebView.route('/user', methods=['GET'])
def user_handler():
    pass
@WebView.route('/event', methods=['POST'])
def event_register():
    try:
        data = request.json
        controller = WebController()
        controller._register_event(data)      
    except Exception as e:
        print(e)
    pass 

@WebView.route('/event', methods=['POST'])
def event_handler():
    pass

@WebView.route('/event_vote')
def event_vote():
    pass


