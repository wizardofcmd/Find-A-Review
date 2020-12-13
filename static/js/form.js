$(document).ready(function(){
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
              loadcanvas();
              insertData();
            }
        });

    
    });
});
