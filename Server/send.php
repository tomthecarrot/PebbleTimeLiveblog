<?php

/**
	PebbleTimeLiveblog code by Thomas Suarez.
	Open-Source License. See LICENSE file for more information.
	
	NOTE: This must be run on a PHP server. If you try this on your local machine,
			it might not work.
**/

### From HTML ###
$status = $_GET['status'];
$mode = $_GET['mode'];

### Pin URL ###
$url = 'https://timeline-api.getpebble.com/v1/shared/pins/YOUR_PIN_ID';

### Pebble Server Topic ###
$topicT = 'YOUR_TOPIC_TITLE';
$topicX = 'YOUR_TOPIC_ID';

### Pebble Server API Keys
$devapikey = 'YOUR_DEVELOPMENT_API_KEY';
$liveapikey = 'YOUR_PRODUCTION_API_KEY';
echo $mode;
if ($mode == 'DEV') {
	$apikey = $devapikey;
}
else {
	$apikey = $liveapikey;
}

### Set this PHP executable to UTC Timezone. Then format outgoing date. ###
date_default_timezone_set("UTC");
$time = date('Y-m-d\TH:i:s\Z');

## Create array for the values ##
$arr = array('id' => 'YOUR_PIN_ID', 'time' => $time, 'layout' => array('type' => 'genericPin',
		'title' => $topicT, 'subtitle' => $status, 'tinyIcon' => 'system://images/NEWS_EVENT'));

## JSON Encode ##
$json = json_encode($arr);

### Curl PUT request to Pebble Server ###
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json', 'X-API-Key: '.$apikey, 'X-Pin-Topics: '.$topicX));
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
echo curl_exec($ch);

?>