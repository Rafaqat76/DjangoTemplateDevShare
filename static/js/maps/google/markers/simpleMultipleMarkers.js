/* ------------------------------------------------------------------------------
*
*  # Basic markers
*
*  Specific JS code additions for maps_google_markers.html page
*
*  Version: 1.0
*  Latest update: Aug 1, 2015
*
* ---------------------------------------------------------------------------- */

$(function() {

	// Setup map
	function initialize() {

		// Set coordinates
		var myLatlng = new google.maps.LatLng(-33, 151);

		// Options
		var mapOptions = {
			zoom: 10,
			center: myLatlng
		};

		 var locations = [
		  ['Bondi Beach', -33.890542, 151.274856, 4],
		  ['Coogee Beach', -33.923036, 151.259052, 5],
		  ['Cronulla Beach', -34.028249, 151.157507, 3],
		  ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
		  ['Maroubra Beach', -33.950198, 151.259302, 1]
			];
			
			
		var map = new google.maps.Map($('.map-marker-simple')[0], {
		zoom: 10,
		center: new google.maps.LatLng(-33.92, 151.25)
		//var contentString = 'Amsterdam';
		
		});	
			
			
			
		// Apply options
		//var map = new google.maps.Map($('.map-marker-simple')[0], mapOptions);
		//var contentString = 'Amsterdam';

		// Add info window
		var infowindow = new google.maps.InfoWindow({
			//content: contentString
		});

		// Add marker
		var marker, i;

		for (i = 0; i < locations.length; i++) {  
		  marker = new google.maps.Marker({
			position: new google.maps.LatLng(locations[i][1], locations[i][2]),
			map: map
		  });

		  google.maps.event.addListener(marker, 'click', (function(marker, i) {
			return function() {
			  infowindow.setContent(locations[i][0]);
			  infowindow.open(map, marker);
			}
		  })(marker, i));
		}
		
				
		
	};

	// Initialize map on window load
	google.maps.event.addDomListener(window, 'load', initialize);

});
