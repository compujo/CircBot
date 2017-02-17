#This script is licensed under the Apace 2.0 License (http://www.apache.org/licenses/LICENSE-2.0)
#This script is a derivative work of the script at https://developers.google.com/api-client-library/python/auth/installed-app

import json
import webbrowser
import configparser
import httplib2
from oauth2client import client

flow = client.flow_from_clientsecrets(
	'client_secrets.json',
	scope='https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl',
	redirect_uri='urn:ietf:wg:oauth:2.0:oob')

auth_uri = flow.step1_get_authorize_url()
webbrowser.open(auth_uri)

print "Opening web browser to request auth code"
auth_code = raw_input('Enter the auth code: ')

credentials = flow.step2_exchange(auth_code)
http_auth = credentials.authorize(httplib2.Http())

outFile = open("OAuthCredentials.json","w")
outFile.write(str(credentials.to_json()))
outFile.close()

# outFile = open("authcode.txt","w")
# outFile.write(auth_code)
# outFile.close()
#
# outFile = open("token.txt","w")
# outFile.write(str(credentials.get_access_token()))
# outFile.close()
