#!/bin/bash
# takes URL, methods accepted by server
curl -Is "$1" | grep "Allow" | cut -d " " -f 2- 
