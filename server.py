'''
PebbleTimeLiveblog Server.
Code by Thomas Suarez (tomthecarrot)
'''

import time as t
import requests as r
from datetime import datetime, date, time

url = "" # replace this with desired liveblog URL

url = url + "/live.json"; # do not modify

### Current Status (liveblog update) from The Verge
status = ""

# DEV: 0
# LIVE: 1
mode = 0

### Pin URL ###
pinID = "verge_live"
url = ("https://timeline-api.getpebble.com/v1/shared/pins/" + pinID)

### Pebble Server Topic ###
topicT = "The Verge Live"
topicX = "verge_live"

### Pebble Server API Keys
devapikey = "YOUR_DEVELOPMENT_API_KEY"
liveapikey = "YOUR_PRODUCTION_API_KEY"

def update():
	status = "test"
	send();

def send():
	### Get and Format current time ###
	isotime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z" # format UTC to make ISO

	### Prepare data payload ###
	layout = { 'type' : 'genericPin', 'title' : topicT, 'subtitle' : status, 'tinyIcon' : 'system://images/NEWS_EVENT', "secondaryColor" : "blue", "backgroundColor" : "white" }
	data = { 'id' : pinID, 'time' : isotime, 'layout' : layout }
	
	### Send to Server ###
	print(data)


### Repeat ###
while True:
	update()
	t.sleep(5) # sleep 5 seconds before next update from server