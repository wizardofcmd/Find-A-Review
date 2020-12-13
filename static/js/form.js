$(document).ready(function(){
    $("#notFound").hide();
    $( "#btn-search" ).click(function() {
        $.ajax({
            data : {
                rv : $('#reviewInput').val()},
            type : 'POST',
            url : '/process'
        })
        .done(function(data){
            if(data.success == "true"){
                $("#notFound").hide();
              absolutelyDestroyCanvas();
              loadcanvas();
              insertData();
            }
            else if(data.success == "false"){
                absolutelyDestroyCanvas();
                createcanvas();
                $("#notFound").show();
            }
        });


    });
});
