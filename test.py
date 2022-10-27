import json
import requests


url = "https://line-chat-bot-1114.herokuapp.com/webview/event_view"
url_local = "http://127.0.0.1:5000/webview/event_view"
json_data = {

	"room_id":"Cdf358fb1484640975bef1fee49ad3920"#jfladjfa
}
headers = headers = {'content-type': 'application/json'}
result = requests.post(url=url,json=json_data,headers=headers)
print(result.json())

"Cdf358fb1484640975bef1fee49ad3920"