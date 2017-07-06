$(document).ready(function(){

    $('button').click(function(){
        var color = $(this).val();
        $.ajax({
            url: '/ninja_color',
            data: color, 
            type: 'POST',
        });
    });
    
});