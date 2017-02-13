import sys
import json
import time
import configparser
import requests

debug = 0

config = configparser.ConfigParser()
config.read('config.ini')
nextPageToken = ''

tokenFile = open("token.txt","r")
token = tokenFile.read()

while (True):
	
	liveChatID = config["OAuth"]["liveChatID"]
	url = 'https://content.googleapis.com/youtube/v3/liveChat/messages?liveChatId='+liveChatID+'&part=snippet,authorDetails&pageToken='+nextPageToken
	
	headers = { 'referer' : '', "Authorization": "Bearer "+config["OAuth"]["token"] }
	
	r = requests.get(url, headers=headers)
	
	resp = r.json()
	if (debug >= 2):
		print json.dumps(resp, indent=4, sort_keys=True)
	
	nextPageToken = resp["nextPageToken"]
	
	msgs = resp["items"]
	
	for msg in msgs:
		print '<'+msg["authorDetails"]["displayName"]+'> '+msg["snippet"]["displayMessage"]
	
	delay_ms = resp['pollingIntervalMillis']
	delay = float(float(delay_ms)/1000)
	
	time.sleep(delay)