#!/bin/bash
# sends a request in silent mode and displays byte size
curl -s "$1" | wc -c
