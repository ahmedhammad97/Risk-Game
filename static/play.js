//WebSocket
var socket = new WebSocket('ws://' + window.location.host + window.location.pathname);

socket.onopen = function(e){
    console.log("Connection started .. Hell yeah!");
};

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    if(data.type=="deployInputRequest") getDeployInput(data);
    if(data.type=="attackInputRequest") getAttackInput(data);
    if(data.type=="render") render(data);
};

socket.onclose = function(e) {
    alert("Something gone wrong, we apologize :(");
};

socket.onerror = function(e) {
    alert("Something gone wrong, we apologize :(");
};

//socket.send("message"); Use Json

//Helper functions
function render(data){
  nodes = data.nodes;
  for(i=0; i<nodes.length; i++){
    $("#"+i).css("background-color", ()=>{
      return nodes[i]["color"]=="Blue"? "dodgerblue" : "red";
    })
    $("#"+i).text(nodes[i]["armies"])
  }
  socket.send(JSON.stringify({"message": "started"}))
}
