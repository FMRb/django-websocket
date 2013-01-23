//socket.io specific code
var socket = io.connect('/update');

socket.on('broadcast',function(msg){
	message("Server", msg);
});

socket.on('error', function(e){
	message("System: ",e ? e : "Error trying to connect");
});

socket.on('test',function(msg){
	message("Testing", msg);
	socket.emit('user send', msg);
});

function message (from, msg){
	$('#message-user').empty();
	$('#message-user').append($('<p>').append($('<b>').text(from), msg));
}

// DOM manipulation
$(function () {
    $('#send-text').submit(function () {
		message('me: ', $('#infoarea').val());
		socket.emit('user send', $('#infoarea').val());
		$('#message-user').css('display','block');
        return false;
    });
});
