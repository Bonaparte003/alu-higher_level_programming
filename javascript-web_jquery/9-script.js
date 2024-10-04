#!/usr/bin/node

$.ajax({
url: 'https://api.allorigins.win/get?url=https://fourtonfish.com/hellosalut/?lang=fr',
type: 'GET',
dataType: 'json',
success: (response) => {
const json = JSON.parse(response.contents);
$('div#hello').text(json.hello);
},
error: (err) => {
console.log('Error:', err);
}
});