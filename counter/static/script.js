$(document).ready(function(){

    $('button').click(function(){
        var modify = $(this).val();
        console.log (modify)
        window.location.assign('/modify/' + modify);
    });
        
});