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
            console.log(data.success);
            if(data.success == "true"){
                $("#notFound").hide();
              console.log("sdfhosdahu");
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
