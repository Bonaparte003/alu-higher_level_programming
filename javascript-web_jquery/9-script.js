$(document).ready(function(){
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data){
        console.log(data.hello);
        $("DIV#hello").text(data.hello);
    });
});