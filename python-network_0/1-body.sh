#!/bin/bash
# GET response, displays only the status code
curl -sL -o /null/dev -w "%{http_code}" "$1"
