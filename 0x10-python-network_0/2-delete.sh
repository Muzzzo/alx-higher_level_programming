#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a DELETE request and display the body
response=$(curl -X DELETE -s "$url")

# Display the body of the response
echo "$response"
