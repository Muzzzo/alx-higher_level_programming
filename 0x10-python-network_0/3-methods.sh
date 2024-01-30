#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send an OPTIONS request and display the Allow header
allow_header=$(curl -sI -X OPTIONS "$url" | grep -i "Allow:")

# Check if "Allow" header is present
if [ -z "$allow_header" ]; then
    echo "Error: 'Allow' header not found in the response."
    exit 1
fi

# Extract and display the allowed HTTP methods
echo "Allowed HTTP Methods for $url: $(echo "$allow_header" | cut -d " " -f 2-)"
