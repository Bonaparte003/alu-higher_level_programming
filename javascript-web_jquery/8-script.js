#!/usr/bin/node
$(document).ready(function(){
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
        for (const film of data.results) {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        }
    })
});