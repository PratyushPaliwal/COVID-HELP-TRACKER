$(document).ready(function(){
 
	if( navigator.geolocation )
	 navigator.geolocation.getCurrentPosition(success);
	else
	$("p").html("HTML5 Not Supported");
 
});
 
function success(position)
{
	$("p").html("Latitude: "+position.coords.latitude+
	            "<br />Longitude: "+position.coords.longitude+
				"<br />Accuracy: "+position.coords.accuracy);

				var location = {latitude: position.coords.latitude, longitude: position.coords.longitude};
				 
				var json = JSON2.stringify(location); 
				//var text = "text to send";
				$.ajax({
					url:'test',
					type:'POST',
					data:{json : json, csrfmiddlewaretoken: '{{ csrf_token }}'},
					//data: json, //{text : text, csrfmiddlewaretoken: '{{ csrf_token }}'},
					dataType: "json",
					success:function (data) {
						console.log("Ajax test success");
						console.log(data);
					},
			
					error:function () {
						console.log("Ajax test failure")
					}
				})
				
				//var text = "text to send";
				
}
/*function ajaxTest(){
	var location = {latitude: position.coords.latitude, longitude : position.coords.longitude};

    var json = JSON2.stringify(location); 
	//var text = "text to send";
	$.ajax({
		url:'test',
		type:'POST',
		data:{json : json, csrfmiddlewaretoken: '{{ csrf_token }}'},
		//data: json, //{text : text, csrfmiddlewaretoken: '{{ csrf_token }}'},
		dataType: "json",
		success:function (data) {
			console.log("Ajax test success");
			console.log(data);
		},

		error:function () {
			console.log("Ajax test failure")
		}
	})
}*/