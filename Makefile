APP="line-chat-bot-1114"

stop:
	heroku ps:scale web=0 --app $(APP)

app:
	heroku ps --app $(APP)

deb:
	export MY_CHANNEL_ACCESS_TOKEN=""
	export MY_CHANNEL_SECRET=""