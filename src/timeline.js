/*
Liveblog App for Pebble Time.
Code by Thomas Suarez (tomthecarrot)
*/

Pebble.addEventListener('ready',
  function(e) {
    console.log('JavaScript app ready and running!');
    
    /*Pebble.getTimelineToken(
      function (token) {
      console.log('My timeline token is ' + token);
    },
    function (error) { 
      console.log('Error getting timeline token: ' + error);
    }
    );*/
    
    Pebble.timelineSubscribe('verge-live', 
      function () { 
        console.log('Subscribed to topic!');
      }, 
      function (errorString) { 
        console.log('Error subscribing to topic: ' + errorString);
      }
    );
  }
);