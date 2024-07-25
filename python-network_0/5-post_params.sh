#!/bin/bash
# sends the POST, displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
