$(document).ready(function() {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function() {
      console.error('An error occurred while fetching the data.');
    }
  });
});