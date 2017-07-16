$(function() {

	// Activate our navbar buttons
	let path = window.location.pathname;
	if (path == '/about') {
		$("#about").addClass('active');
		$("#home").removeClass('active');
	} else {
		$("#home").addClass('active');
		$("#about").removeClass('active');
	}

	// call /get_page to do the work and return the image filename
	$("#get_page").click(function(event) {
		event.preventDefault();
		let page_url = $("#req_url").val();
		let page_width = $("#req_width").val();
		let page_height = $("#req_height").val();
		
		// lazy validation
		if (page_url == '') {
			return;
		}

		$("#callback_url").removeAttr('hidden');
		$("#callback_url").addClass('btn-warning loading-animation')
		$("#callback_url").text("Doing the magic...")
		$.ajax({
			url: '/api/grab',
			headers: {
				'key':'super secret key right here that does nothing',
			},
			type: 'POST',
			data: 
				{
					url: page_url,
					width: page_width,
					height: page_height,
				},
			dataType: 'json',
		})
		// , page_width: req_width, page_height: req_height
		.done(function(data) {
			$("#callback_url").removeClass('loading-animation btn-warning');
			$("#callback_url").addClass('btn-success');
			$("#callback_url").attr('href',"/static/screenshots/"+data['url']);
			$("#callback_url").text("Ta-Da! Click to view.");
		})
		.fail(function() {
			$("#callback_url").addClass('btn-danger');
			$("#callback_url").removeClass('loading-animation btn-warning');
			$("#callback_url").text("Something went wrong :(");
		})
		.always(function() {
			console.log("complete");
		});	
	}); //end ajax

	// Toggle options
	$("#toggle_options").click(function(event) {
		$("#options_div").toggle("fast");
	});

}); //end doc