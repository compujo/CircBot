# CircBot
YouTube LiveStream Chatbot 

# Quickstart
1. Make sure Python 2.7 is installed and pip install any dependencies as they come up (configparser, requests, etc)
2. Make a new project with the [Google API Console](https://console.developers.google.com/apis/) and enable the Youtube Data API.  
3. Add OAuth API credentials, download the JSON file and save it as client_secrets.json in the project folder
4. Run auth.py ("python auth.py") to get an auth code and token
5. Depending on the state of the project, you may need to manually get the token from token.txt and put it in config.ini, check the code for where exactly
6. Get your live chat ID using https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list and put it in config.ini
7. Run main.py ("python main.py")
8. Token expiration time is not yet accounted for, so the bot will probably need re auth and restart every hour or so


# Related Documentaion and Links
https://developers.google.com/youtube/v3/live/docs/liveChatMessages
https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list
https://developers.google.com/youtube/v3/live/getting-started
https://developers.google.com/api-client-library/python/auth/installed-app

http://docs.python-requests.org/en/latest/user/quickstart/