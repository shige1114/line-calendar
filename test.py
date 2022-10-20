import requests


url = "https://line-chat-bot-1114.herokuapp.com/webview/event_view"
json_data = {
	"room_id":"Cdf358fb1484640975bef1fee49ad3920"
}

requests.get(url=url)

