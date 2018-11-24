var socket = new WebSocket('ws://' + window.location.host +
                                     window.location.pathname);

socket.onopen = function(e){
    console.log("Connection started .. Hell yeah!");
};

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    if(data.type=="deployInputRequest") getDeployInput(data);
    if(data.type=="attackInputRequest") getAttackInput(data);
    if(data.type=="renderDeployments") renderDeployments(data);
    if(data.type=="renderAttack") renderAttack(data);
    if(data.type=="render") render(data);
    if(data.type=="winning") displayMessage(data.message, data.winner)
};

socket.onclose = function(e) {
    alert("Something gone wrong, we apologize :(");
};

socket.onerror = function(e) {
    alert("Something gone wrong, we apologize :(");
};

//Helper functions
function displayMessage(message, color){
  $('#msg').text(message)
  $('#msg').css("color", ()=>{return color=="Blue" ? "dodgerblue" : "red"})
}

function render(data){
  nodes = data.nodes;
  for(i=0; i<nodes.length; i++){
    $("#"+i).css("background-color", ()=>{
      return nodes[i]["color"]=="Blue"? "dodgerblue" : "red";
    })
    $("#"+i).text(nodes[i]["armies"])
  }
}

function renderDeployments(data){
  displayMessage(data.message, data.color);
  render(data);
  socket.send(JSON.stringify({"type" : "deploymentSuccess"}))
}

function renderAttack(data){
  displayMessage(data.message, data.color);
  render(data);
  socket.send(JSON.stringify({"type" : "attackSuccess"}))
}
