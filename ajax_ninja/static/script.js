$(document).ready(function(){

    $('button').click(function(){
        var color = $(this).val();
        $.getJSON('/process/' + color, function(result){
            var turtle = result.color;
            switch(turtle){
                case 'red':
                    $('#ninja_pics').html("<h1>You chose Raphael!</h1><img src='../static/ninjas/raphael.jpg'>");
                    break;
                case 'blue':
                    $('#ninja_pics').html("<h1>You chose Leonardo!</h1><img src='../static/ninjas/leonardo.jpg'>");
                    break;
                case 'orange':
                    $('#ninja_pics').html("<h1>You chose Michelangelo!</h1><img src='../static/ninjas/michelangelo.jpg'>");
                    break;
                case 'purple':
                    $('#ninja_pics').html("<h1>You chose Donatello!</h1><img src='../static/ninjas/donatello.jpg'>");
                    break;
                default:
                    $('#ninja_pics').html("<h1>There's no ninja in that color!</h1><img src='../static/ninjas/notapril.jpg'>");
                    break;
            }
        });
    });

});