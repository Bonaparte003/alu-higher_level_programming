#!/bin/bash
# GET response, displays only the status code
curl -s -o /null/dev -w "%{http_code}" "$1"
