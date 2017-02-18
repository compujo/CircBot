import sys
import os.path
import json
import time
import configparser
import requests

#OAuth2 libs
import httplib2
from oauth2client import client

def get_livechat_id():
	# Authenticate

	if (not os.path.isfile("OAuthCredentials.json")):
		import auth

	credentialsFile = open("OAuthCredentials.json","r")
	credentialsJSON = credentialsFile.read()

	credentials = client.OAuth2Credentials.from_json(credentialsJSON)

	token_obj = credentials.get_access_token()
	token_str = str(token_obj.access_token)

	url = 'https://content.googleapis.com/youtube/v3/liveBroadcasts?broadcastStatus=active&broadcastType=all&part=id%2Csnippet%2CcontentDetails'

	headers = { "Authorization": "Bearer "+token_str }

	r = requests.get(url, headers=headers)

	if (r.status_code == 200):
		resp = r.json()
		if (len(resp["items"]) <= 0):
			return False
		else:
			# Success, get the id and save
			
			# Should only be 1 item unless YT adds multiple livestreams, then we'll assume it's the first for now
			streamMeta = resp["items"][0]["snippet"] 
			liveChatID = streamMeta["liveChatId"]
			return liveChatID
	else:
		print("Unrecognized error:\n")
		resp = r.json()
		print(json.dumps(resp, indent=4, sort_keys=True))

if __name__ == '__main__':
	liveChatID = get_livechat_id()
	if (liveChatID == False):
		print("No livestream found :(")
		sys.exit(1)
	print liveChatID