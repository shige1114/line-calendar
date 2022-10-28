from statistics import mode
from sys import flags
from flask import Blueprint, flash, jsonify, redirect, request, url_for
import requests
from src.MVC.controller.WebController import WebController
import json
from src.MVC.models.MySqlDriver import MySqlDriver

WebView = Blueprint('webview',__name__,url_prefix='/webview')


@WebView.route('/', methods=['GET'])
def index():

    return '<h1>k<h1>'
@WebView.route('/login',methods=['GET'])
def login():

    pass
@WebView.route('/event_view', methods=['POST'])
def event_view():
    model = MySqlDriver()
    print(request.json,flush=True)
    
    room_id = str(request.json["room_id"])
    calendar=model._get_calendar(id=room_id)
    if calendar:
        calendar = calendar.to_dict()
    
    events = model._search_events(room_id)
    if events:
        events = [ e.to_dict() for e in events ]
    print(calendar,flush=True)
    data = {"calendar":calendar,"events":events}
    
    return jsonify(data)
    
    pass
@WebView.route('/event_edit',methods=['POST'])
def event_edit():
    model = MySqlDriver()
    print(request.json,flush=True)
    status=model._register_event(**request.json)

    if status:
        return jsonify({"status":"succes"})
    else:
        return jsonify({"status":"fail"})


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
    model = MySqlDriver()
    model._create_user()
    return 200

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

@WebView.route('/event_vote',methods=['POST'])
def event_vote():
    
    model = MySqlDriver()
    model._vote_event(**request.json)

    return jsonify({"status":"secces"})

    

    pass



    



