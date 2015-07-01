'''
PebbleTimeLiveblog Server.
Code by Thomas Suarez (tomthecarrot)
'''

from datetime import datetime, date, time
import time as t
import requests
import json


### USER-DEFINED VARS ###

# Replace this with desired liveblog URL:
liveblog = "http://live.theverge.com/google-io-atap-regina-dugan-liveblog-2015/"

# DEV: 0
# LIVE: 1
mode = 0

### Ask for API key at runtime? ###
# this will override any api keys set below, for that runtime!
askforkey = True

# Number of seconds to wait between updates
timeout = 5

#################################################

styleBold = '\033[1m'
styleEnd = '\033[0m'
print(styleBold + "PebbleTimeLiveblog Server" + styleEnd)

#################################################

### Last received liveblog update (status) from The Verge ###
status = "Hello World"

### Concatenate: liveblog URL + absolute file path ###
liveblog = liveblog + "live.json" # do not modify

### Pin URL ###
pinID = "verge_live"
pinURL = ("https://timeline-api.getpebble.com/v1/shared/pins/" + pinID)

### Pebble Server Topic ###
topicT = "The Verge Live"
topicX = "verge-live"

### Pebble Server API Keys
apikey = ""
devapikey = "YOUR_DEVELOPMENT_API_KEY"
liveapikey = "YOUR_PRODUCTION_API_KEY"

### Auto-choose API Key based on mode ###
if mode is 0:
	apikey = devapikey
else:
	apikey = liveapikey

### Ask for API key at runtime, if stated in above var. ###
if askforkey:
	apikey = input("Insert API Key: ")

#################################################

def update():
	global status  # set this var globally
	status = input("Insert New Status: ") #tmp test
	send()

def send():
	### Get and Format current time ###
	isotime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z" # format UTC to make ISO time

	### Prepare data payload ###
	layout = { 'type' : 'genericPin', 'title' : topicT, 'subtitle' : status, 'tinyIcon' : 'system://images/NEWS_EVENT', "secondaryColor" : "blue", "backgroundColor" : "white" }
	payload = { 'id' : pinID, 'time' : isotime, 'layout' : layout }
	headers = { 'Content-Type' : 'application/json', 'X-API-Key' : apikey, 'X-Pin-Topics' : topicX }
	
	### Send to Pebble Server ###
	print("Sending to Pebble: " + status)
	r = requests.put(pinURL, data=json.dumps(payload), headers=headers)
	print(r.text) # log response (should be 'OK')


### Repeat ###
while True:
	update()
	print("Wait...")
	t.sleep(timeout) # sleep 5 seconds before next update from server