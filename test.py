import json
import requests


url = "https://line-chat-bot-1114.herokuapp.com/webview/register_days"
url_local = "http://127.0.0.1:5000/webview/event_view"
json_data = {

    "data": [0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0, ]  # jfladjfa
}
headers = headers = {'content-type': 'application/json'}
result = requests.post(url=url, json=json_data, headers=headers)
print(result.json())

"Cdf358fb1484640975bef1fee49ad3920"
