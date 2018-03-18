 
      var map;
      var pyrmont = {lat: -2.191198, lng:-79.882160};
          
    function initialize() {
         map = new google.maps.Map(document.getElementById('map'), {
            center: pyrmont,
            zoom: 14
        });
        
        infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);
        service.nearbySearch({
          location: pyrmont,
          radius: 1000,
          type: ['store']
        }, callback);

        
      
    }
      function callback(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
            }
        }
    }
    function createMarker(place) {
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });

        google.maps.event.addListener(marker, 'click',function(){
            infowindow.setContent(place.name);
            infowindow.open(map,this);
            
        var panorama = new google.maps.StreetViewPanorama(
            document.getElementById('pano'), {
                position: place.geometry.location,
                pov: {
                heading: 34,
                pitch: 10
                }
            });
        map.setStreetView(panorama);
            
    
            })
    }
/*key=AIzaSyBg4Atm6V-CN0yBOFzBhPwXBwIs-V8pNQo
function initMap() {
    
     map = new google.maps.Map(document.getElementById('map'), {
       center: pyrmont,
       zoom: 15,
     });*/