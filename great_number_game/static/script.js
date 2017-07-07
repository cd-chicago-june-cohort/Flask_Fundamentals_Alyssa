$(document).ready(function(){

    $('#submit').click(function(){
        var guess = $('#guess').val();
        $('#guess').focus();
        $('#guess').val('');
        $.getJSON('/process/' + guess, function(result){
            console.log(result);
            var feedback = result.feedback;
            $('#feedback').html("<h1>" + feedback + "</h1>");
            $('#feedback').show();
            if (feedback == "Too High" || feedback == "Too Low"){
                $('#feedback').addClass('wrong');
            } else {
                $('#feedback').removeClass('wrong').addClass('right');
                $('#feedback').append('<button id="again">Play Again?</button>');
            }
        });
    });

    $('#feedback').on('click', '#again', function(){
        console.log("play again");
        $('#feedback').hide();
        window.location.assign('/again');
    });

});