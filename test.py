import json
import requests


url = "https://line-chat-bot-1114.herokuapp.com/webview/event_view"
url_local = "http://127.0.0.1:5000/webview/event_view"
json_data = {
	"room_id":"jfladjfa"
	
}

result = requests.post(url=url_local,json=json_data)
print(result.text)

"Cdf358fb1484640975bef1fee49ad3920"