# PebbleTimeLiveblog
![](https://raw.github.com/tomthecarrot/PebbleTimeLiveblog/master/screenshots/banner.png)  
Liveblog tracker for [Pebble Time](http://getpebble.com).

## Features
- Real-time updates from a custom web server to Pebble Time smartwatches!
- Utilizes new Timeline functionality to quickly deliver automatic updates to your wrist.
- Written in C.
- Open-source license.
- See ["verge" branch](https://github.com/tomthecarrot/PebbleTimeLiveblog/tree/verge) for following the latest liveblogs from The Verge on your Pebble Time.

## Installation
Go to the Pebble App Store on your phone and search for "Liveblog", or [click this link](https://apps.getpebble.com/applications/554ec47cecdc00f8140000c6).

## Usage
1. Before (or during) a live event, install the app on your Pebble Time through the Pebble App Store.
- Once the app is installed on your Pebble Time, open it. It should say "Subscribed".
- Now, just wait for updates!
- They will show up as past updates,
so click the up button on the right side of your Pebble Time.
- Only one card will be pushed for a live event, but it will update continuously.
- Click the middle button on your Pebble Time, and voila!
- Tip: You can keep the card open on your Pebble Time, as it updates itself! Cool, right?
Because of Pebble Time's e-paper screen, keeping the display on won't drain your battery.

## Web Server
1. In the PHP file, replace the indicated values (API keys, etc.) with your own ones.
- Then, upload the entire Server directory to your web server.
- Visit the website and start posting updates!
- Tip: I recommend putting .htaccess & .htpasswd files in that directory, just to make sure unauthorized people
cannot post as you!

## Screenshots
![N/A](https://raw.github.com/tomthecarrot/PebbleTimeLiveblog/master/screenshots/screen1.png)
![N/A](https://raw.github.com/tomthecarrot/PebbleTimeLiveblog/master/screenshots/screen2.png)
![N/A](https://raw.github.com/tomthecarrot/PebbleTimeLiveblog/master/screenshots/screen3.png)

## Uninstall
Uninstall from the Pebble Time app on your phone.

## License
GPL 3.0 License. See LICENSE file for more information.

## Other Works
[Lenny Khazan](https://github.com/LK/PebbleLiveblog) - the developer of an earlier SDK 2 liveblog watchapp.
