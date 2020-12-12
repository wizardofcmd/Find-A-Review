function ajax($this) {
  var book_data = $this.attr('name');
  console.log(book_data);
  var sys = arbor.ParticleSystem(10, 400, 1);
  sys.parameters({
    gravity: false,
    repulsion: 150
  });
  sys.renderer = Renderer("#viewport");


}
$(document).ready(function(){
    $( "#btn-search" ).click(function() {
        $.ajax({
            data : {
                rv : $('#reviewInput').val()},
            type : 'POST',
            url : '/process'
        })
        .done(function(data){
var data = JSON.stringify(data);

        });

        event.preventDefault();
    });
});
// Have a function that creates element instead to refresh canvas
function loadcanvas(id) {
  var canvas = document.createElement('canvas');
  var div = document.getElementById(id)
  canvas.id = "viewport";
  canvas.width = "1108";
  canvas.height = "688";
  canvas.class = "model-content"
  div.appendChild(canvas);
}
// Still don't know how to refresh so instead, delete the canvas
function absolutelyDestroyCanvas(id) {
  var elem = document.getElementById(id);
  elem.parentNode.removeChild(elem);
}
