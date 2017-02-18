import sys
import os.path
import json
import time
import configparser
import requests
import getLiveChatID

#OAuth2 libs
import httplib2
from oauth2client import client

config = configparser.ConfigParser()
config.read('config.ini')

with open("config.json") as jsonFile:
	configJSON = json.load(jsonFile)

# Message handler
def handle_msg(msg):
	wlWords = configJSON["whitelistFilter"]
	for word in wlWords:
		if word in msg["snippet"]["displayMessage"]:
			print '<'+msg["authorDetails"]["displayName"]+'> '+msg["snippet"]["displayMessage"]
			return



debug = int(config["Settings"]["debug"])

# Authenticate

if (not os.path.isfile("OAuthCredentials.json")):
	import auth
	os.system('cls')

credentialsFile = open("OAuthCredentials.json","r")
credentialsJSON = credentialsFile.read()

credentials = client.OAuth2Credentials.from_json(credentialsJSON)

token_obj = credentials.get_access_token()
token_str = str(token_obj.access_token)

# End of authentication

liveChatID = getLiveChatID.get_livechat_id()
if (liveChatID == False):
	print("No livestream found :(")
	sys.exit(1)

nextPageToken = ''

while (True):

	# Make sure access token is valid before request
	if (credentials.access_token_expired):
		# Access token expired, get a new one
		token_obj = credentials.get_access_token() #get_access_token() should refresh the token automatically
		token_str = str(token_obj.access_token)

	url = 'https://content.googleapis.com/youtube/v3/liveChat/messages?liveChatId='+liveChatID+'&part=snippet,authorDetails&pageToken='+nextPageToken

	headers = { "Authorization": "Bearer "+token_str }

	r = requests.get(url, headers=headers)

	if (r.status_code == 200):
		resp = r.json()
		if (debug >= 2):
			print json.dumps(resp, indent=4, sort_keys=True)

		nextPageToken = resp["nextPageToken"]

		msgs = resp["items"]

		for msg in msgs:
			#Message handling
			handle_msg(msg)

		delay_ms = resp['pollingIntervalMillis']
		delay = float(float(delay_ms)/1000)

	elif (r.status_code == 401):
		#Unauthorized
		delay = 10

		if (credentials.access_token_expired):
			# Access token expired, get a new one
			if (debug >= 1):
				print "Access token expired, obtaining a new one"

			token_obj = credentials.get_access_token() #get_access_token() should refresh the token automatically
			token_str = str(token_obj.access_token)
		else:
			print "Error: Unauthorized. Trying again in 30 seconds... (ctrl+c to force quit)"
			resp = r.json()
			if (debug >= 1):
				print json.dumps(resp, indent=4, sort_keys=True)

			delay = 30

	else:
		print("Unrecognized error:\n")
		resp = r.json()
		print(json.dumps(resp, indent=4, sort_keys=True))
		delay = 30

	time.sleep(delay)
