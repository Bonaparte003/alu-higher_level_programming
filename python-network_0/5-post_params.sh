#!/bin/bash
# sends the POST, displays the body of the response
curl -X POST -d "email=test@gmail.com&data=I will always be here for PLD" "$1"
