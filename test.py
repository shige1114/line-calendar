import json
import requests


url = "https://line-chat-bot-1114.herokuapp.com/webview/register_days"
url_local = "http://127.0.0.1:5000/webview/event_view"
url = "https://line-chat-bot-1114.herokuapp.com/webview/register_days"
headers = {'content-type': 'application/json'}
json_data = {
    "data": [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0
    ]
}

result = requests.post(url=url, json=json_data, headers=headers)
print(result.status_code)

"Cdf358fb1484640975bef1fee49ad3920"
