#!/usr/bin/node
$(document).ready(function() {
  $('DIV#red_header').on('click', function() {
    $('header').addClass('red');
  });
});