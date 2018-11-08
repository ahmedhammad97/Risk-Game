//WebSocket
var socket = new WebSocket('ws://' + window.location.host + window.location.pathname);

socket.onopen = function(e){
    console.log("Connection started .. Hell yeah!");
};

socket.onmessage = function(e) {
    var data = e.data;
    //var message = data['message'];
    console.log(data);
    //TBC
};

socket.onclose = function(e) {
    alert("Something gone wrong, we apologize :(");
};

socket.onerror = function(e) {
    alert("Something gone wrong, we apologize :(");
};

//socket.send("message"); Use Json
