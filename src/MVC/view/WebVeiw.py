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

@WebView.route('/event_view', methods=['POST'])
def event_view():
    model = MySqlDriver()
    print(request.json,flush=True)
    
    group_id = str(request.json["group_id"])
    calendar=model._get_calendar(group_id=group_id)
    if calendar:
        calendar = calendar.to_dict()
    
    events = model._search_events(group_id)
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

@WebView.route('/event_vote',methods=['POST'])
def event_vote():
    print(request.json,flush=True) 
    model = MySqlDriver()
    model._vote_event(**request.json)

    return jsonify({"status":"secces"})
    pass

@WebView.route('/get_days',methods=['POST'])
def get_days():
    model = MySqlDriver()
    try:
        days = model._get_days(0)
        return jsonify(days)
    except Exception:
        print("model error",flush=True)
    return '<h1>1</h1>'

@WebView.route('/register_days',methods=['POST'])
def register_days():
    model = MySqlDriver()
    print(request.json)
    
    days = model._register_days(request.json)
    return jsonify(days)
    


    



