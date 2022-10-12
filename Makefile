APP="line-chat-bot-1114"
OPTIONS_APP=--app line-chat-bot-1114

stop:
	heroku ps:scale web=0 --app $(APP)

app:
	heroku ps --app $(APP)

start:
	heroku ps:scale web=1 $(OPTIONS_APP)
open:
	heroku domains $(OPTIONS_APP)

deb:
	export MY_CHANNEL_ACCESS_TOKEN=""
	export MY_CHANNEL_SECRET=""