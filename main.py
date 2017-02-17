import sys
import os.path
import json
import time
import configparser
import requests

#OAuth2 libs
import httplib2
from oauth2client import client

config = configparser.ConfigParser()
config.read('config.ini')

debug = config["Settings"]["debug"]

# Authenticate

if (not os.path.isfile("OAuthCredentials.json")):
	#print "Please run auth.py first to obtain credentials"
	#sys.exit(1)
	import auth

credentialsFile = open("OAuthCredentials.json","r")
credentialsJSON = credentialsFile.read()

credentials = client.OAuth2Credentials.from_json(credentialsJSON)
http_auth = credentials.authorize(httplib2.Http())

token_obj = credentials.get_access_token()
token_str = str(token_obj.access_token)

nextPageToken = ''
liveChatID = config["Stream"]["liveChatID"]

while (True):

	# Make sure access token is valid before request
	if (credentials.access_token_expired):
		# access token expired, get a new one
		token_obj = credentials.get_access_token() #get_access_token() should refresh the token automatically
		token_str = str(token_obj.access_token)

	url = 'https://content.googleapis.com/youtube/v3/liveChat/messages?liveChatId='+liveChatID+'&part=snippet,authorDetails&pageToken='+nextPageToken

	headers = { 'referer' : '', "Authorization": "Bearer "+token_str }

	r = requests.get(url, headers=headers)

	if (r.status_code == 200):
		resp = r.json()
		if (debug >= 2):
			print json.dumps(resp, indent=4, sort_keys=True)

		nextPageToken = resp["nextPageToken"]

		msgs = resp["items"]

		for msg in msgs:
			#Message handling
			print '<'+msg["authorDetails"]["displayName"]+'> '+msg["snippet"]["displayMessage"]

		delay_ms = resp['pollingIntervalMillis']
		delay = float(float(delay_ms)/1000)

	elif (r.status_code == 401):
		#Unauthorized
		delay = 10

		if (credentials.access_token_expired):
			#access token expired, get a new one
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
