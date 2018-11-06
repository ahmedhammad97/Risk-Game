//Default Map
var egypt = true;
$("#isEgypt").prop("checked", true);

//Toggle Maps
$("#maps img").on("click", event=>{
  var el = event.target;
  if(!$(el).hasClass("selected")){
    $("#maps img").removeClass("selected");
    $(el).addClass("selected");
    egypt = !egypt;
    $("#isEgypt").prop("checked", egypt);
  }
})

$("button").on("click", event=>{
  if(!validateInput()){
    event.preventDefault();
    alert("You need to choose both agents");
  }
})

//Helper Functions
function validateInput(){
  var p1 = $("#playerOne").val();
  var p2 = $("#playerTwo").val();
  if(p1!==null & p2!==null){return true;}
}
