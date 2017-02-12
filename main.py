#!/usr/bin/python

import time
import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

while (True):
	
	url = 'https://content.googleapis.com/youtube/v3/liveChat/messages?liveChatId=EiEKGFVDZmhqblk4YVpkaldCMkc1NC1xR1BVZxIFL2xpdmU&part=snippet&key='
	url += config['main']['yt_api']
	
	headers = { 'referrer' : 'totallyrealwebsite.com' }
	
	r = requests.get(url, headers=headers)
	
	print str(r.json())
	time.sleep(5)