//WebSocket
var socket = new WebSocket('ws://' + window.location.host + window.location.pathname);

socket.onopen = function(e){
    console.log("Connection started .. Hell yeah!");
};

socket.onmessage = function(e) {
    var data = e.data;
    if(data.type=="initialization") initialize(JSON.parse(data));
    if(data.type=="deplyInputRequest") getDeployInput(JSON.parse(data));
    if(data.type=="attackInputRequest") getAttackInput(JSON.parse(data));
    if(data.type=="render") render(JSON.parse(data));
};

socket.onclose = function(e) {
    alert("Something gone wrong, we apologize :(");
};

socket.onerror = function(e) {
    alert("Something gone wrong, we apologize :(");
};

//socket.send("message"); Use Json

//Helper functions
function initialize(data){

}
