var socket = new WebSocket('ws://' + window.location.host +
                                     window.location.pathname);

socket.onopen = function(e){
    console.log("Connection started .. Hell yeah!");
};

socket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    setTimeout(()=>{
      if(data.type=="render") render(data);
      if(data.type=="deployInputRequest") getDeployInput(data);
      if(data.type=="attackInputRequest") getAttackInput(data);
      if(data.type=="renderDeployments") renderDeployments(data);
      if(data.type=="renderAttack") renderAttack(data);
      if(data.type=="winning") displayMessage(data.message, data.winner)
    },1500)
};

socket.onclose = function(e) {
    alert("Connection lost, we apologize :(");
};

socket.onerror = function(e) {
    alert("Something gone wrong, we apologize :(");
};

//Game variables
var allowInput = false;
var mode = true;
var first = true;
var attacker = null;

//Helper functions
function displayMessage(message, color){
  $('#msg').text(message)
  if(color)  $('#msg').css("color", ()=>{return color=="Blue" ? "rgb(30, 144, 255)" : "rgb(255, 0, 0)"})
}

$('.army').on("click", (e)=>{
  if(allowInput){
    if(mode){
      let id = e.target.id;
      let armies = +($('#msg').text().substring(9,10));
      e.target.innerHTML = +(e.target.innerHTML) + armies;
      armies = e.target.innerHTML;
      let color = e.target.style.backgroundColor;
      if(color == $("#msg").css("color")){
        color = color=="rgb(255, 0, 0)"? "Red" : "Blue"
        sendHumanDeployData(id, armies, color);
      }
      else{
        sendError()
      }
    }
    else{
      if(first){
        attacker = e.target
        displayMessage("Now, click on territory to attack");
        first = false;
      }
      else{
        let attacked = e.target
        //Start Processing
        if(+((attacker).innerHTML) > +((attacked).innerHTML) + 1){
          (attacked).innerHTML = (+((attacker).innerHTML)) - (+((attacked).innerHTML)) - 1;
          (attacker).innerHTML = 1;
          (attacked).style.backgroundColor =  (attacker).style.backgroundColor

          //Data to send
          let id1 = (attacker).id;
          let id2 = (attacked).id;
          let armies1 = (attacker).innerHTML;
          let armies2 = (attacked).innerHTML;
          let color1 = (attacker).style.backgroundColor;
          let color2 = (attacked).style.backgroundColor;

          if(color1 != color2){
            color = color=="rgb(255, 0, 0)"? "Red" : "Blue"
            sendHumanAttackData(id1, armies1, color, id2, armies2)
          }
          else{
            sendError()
          }
        }else{
          sendError()
        }
      }
    }
  }
})

function render(data){
  nodes = data.nodes;
  for(let i=0; i<nodes.length; i++){
    $("#"+i).css("background-color", ()=>{
      return nodes[i]["color"]=="Blue"? "rgb(30, 144, 255)" : "rgb(255, 0, 0)";
    })
    let originalArmies = $("#"+i).text()
    $("#"+i).text(nodes[i]["armies"])
    if(originalArmies != $("#"+i).text()){
      let originalColor = $("#"+i).css("background-color")
      $("#"+i).css("background-color", "yellow")
      setTimeout(()=>{$("#"+i).css("background-color", originalColor)}, 1000)
    }
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

function getDeployInput(data){
  allowInput = true
  mode = true
  displayMessage("You have " + data.armies + " bonus armies .. Click a territory to deploy them", data.color)
}

function getAttackInput(data){
  allowInput = true
  mode = false
  first = true
  displayMessage("Your turn to attack .. click on your territory")
}

function sendHumanDeployData(id, armies, color){
  socket.send(JSON.stringify({
    "type" : "deployResponse",
    "updates" : [{
      "id" : id,
      "armies" : armies,
      "color" : color
    }]
  }))
  allowInput = false;
}

function sendHumanAttackData(id1, armies1, color, id2, armies2){
  socket.send(JSON.stringify({
    "type" : "attackResponse",
    "updates" : [{
      "id" : id1,
      "armies" : armies1,
      "color" : color
    },
    {
      "id" : id2,
      "armies" : armies2,
      "color" : color
    }
  ]
  }))
  allowInput = false;
}

function sendError(){
  alert("Invalid move .. turn passed")
  socket.send(JSON.stringify({"type" : "error"}))
}
