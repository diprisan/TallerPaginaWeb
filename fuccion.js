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
          radius: 1500,
          type: ['parking']
        }, callback);
		
        }

       
      

      function callback(results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
          for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
            }
        }
    }
    function createMarker(place) 
	{
        var placeLoc = place.geometry.location;
		var ranMath ;
        var marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });
		google.maps.event.addListener(marker, 'click',function()
		{
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
		ranMath=Math.floor((Math.random() * 100) + 1);
		dibujar(ranMath);
		})
    }


	        function dibujar(randParam) {


            var ctx = document.getElementById('nuestroCanvas');
            var contenido = ctx.getContext('2d');
            var imagenGrafica = new Image();
            imagenGrafica.src = 'grafica.png';
            imagenGrafica.onload = function() {

                //Cargo la imagen en la posici�n

                contenido.drawImage(imagenGrafica, 0, 0, 720, 360);


                //Indicar el grosor de la l�nea

                contenido.lineWidth = 4;

                //Dibujo las l�neas para simular la gr�fica

                contenido.beginPath();


                contenido.moveTo(16, 156);

                contenido.lineTo(77, 66);

                contenido.lineTo(135, 100);

                contenido.lineTo(194, 200);

                contenido.lineTo(255, 185);

                contenido.lineTo(316, 195);

                contenido.lineTo(376, 155);

                contenido.lineTo(436, 185);


                contenido.strokeStyle = "hsla(333, 71%, 53%, 1)";

                contenido.stroke();


                //Indicar el grosor de la l�nea

                contenido.lineWidth = 1;

                //Dibujo las l�neas para simular la gr�fica

                contenido.beginPath();


                contenido.moveTo(16+randParam, 126);

                contenido.lineTo(97+randParam, 176);

                contenido.lineTo(435+randParam, 160);


                contenido.lineTo(294+randParam, 100);

                contenido.lineTo(255+randParam, 155);

                contenido.lineTo(316+randParam, 225);

                contenido.lineTo(376+randParam, 85);

                contenido.lineTo(436+randParam, 185);


                contenido.strokeStyle = "hsla(120, 100%, 50%, 1)";

                contenido.stroke();




            }

        }

        function line() {

            var canvas = document.getElementById('canvasGlowing');
            var context = canvas.getContext('2d');

            var lastX = context.canvas.width * Math.random();
            var lastY = context.canvas.height * Math.random();
            var hue = 0;

            context.save();
            context.translate(context.canvas.width / 2, context.canvas.height / 2);
            context.scale(0.9, 0.9);
            context.translate(-context.canvas.width / 2, -context.canvas.height / 2);
            context.beginPath();
            context.lineWidth = 5 + Math.random() * 10;
            context.moveTo(lastX, lastY);
            lastX = context.canvas.width * Math.random();
            lastY = context.canvas.height * Math.random();
            context.bezierCurveTo(context.canvas.width * Math.random(),
                context.canvas.height * Math.random(),
                context.canvas.width * Math.random(),
                context.canvas.height * Math.random(),
                lastX, lastY);

            hue = hue + 10 * Math.random();
            context.strokeStyle = 'hsl(' + hue + ', 50%, 50%)';
            context.shadowColor = 'white';
            context.shadowBlur = 10;
            context.stroke();
            context.restore();
        }
        setInterval(line, 50);

        function blank() {
            context.fillStyle = 'rgba(0,0,0,0.1)';
            context.fillRect(0, 0, context.canvas.width, context.canvas.height);
        }
        setInterval(blank, 40);
