# CircBot
YouTube LiveStream Chatbot

# Quickstart
1. Make sure Python 2.7 with pip is installed (Python 3 should work but hasn't been tested)
2. pip install configparser oauth2client httplib2 requests
2. Make a new project with the [Google API Console](https://console.developers.google.com/apis/) and enable the Youtube Data API.  
3. Add OAuth API credentials, download the JSON file and save it as client_secrets.json in the project folder
4. Run auth.py ("python auth.py"), approve the OAuth request in your webbrowser, and copy the auth code to the console
5. clear the console ("cls" in Windows)
6. Start the stream so that the bot can fetch the live chat identifier
7. Run main.py ("python main.py")


# Related Documentaion and Links
https://developers.google.com/youtube/v3/live/docs/liveChatMessages
https://developers.google.com/youtube/v3/live/docs/liveBroadcasts/list
https://developers.google.com/youtube/v3/live/getting-started
https://developers.google.com/api-client-library/python/auth/installed-app

http://docs.python-requests.org/en/latest/user/quickstart/
