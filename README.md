# CircBot
YouTube LiveStream Chatbot 

# Quickstart
0. Make sure Python 2.7 is installed and pip install any dependencies as asked (requests, configparser, etc)
1. Make a new project with the [Google API Console](https://console.developers.google.com/apis/) and enable the Youtube Data API.  
2. Add OAuth API credentials, download the JSON file and save it as client_secrets.json in the project folder
3. Run auth.py ("python auth.py") to get an auth code and token
4. Depending on the state of the project, you may need to manually get the token from token.txt and put it in config.ini, check the code for where exactly
5. Get your live chat ID using https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list and put it in config.ini
6. Run main.py ("python main.py")


# Related Documentaion and Links
https://developers.google.com/youtube/v3/live/docs/liveChatMessages
https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list
https://developers.google.com/youtube/v3/live/getting-started

http://docs.python-requests.org/en/latest/user/quickstart/