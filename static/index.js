//Default Map
var egypt = true;

//Toggle Maps
$("#maps img").on("click", event=>{
  var el = event.target;
  if(!$(el).hasClass("selected")){
    $("#maps img").removeClass("selected");
    $(el).addClass("selected");
    egypt = !egypt;
  }
})

$("button").on("click", event=>{
  event.preventDefault();
  if(validateInput()){
    //Here we go...
  }
  else{
    alert("Plase check your input again!");
  }
})

//Helper Functions
function validateInput(){
  var p1 = $("#playerOne").val();
  var p2 = $("#playerTwo").val();
  if(p1!==null & p2!==null){return true;}
}
