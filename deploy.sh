#!/bin/bash

# Pull the latest image
docker pull sarathkumar455/goodluckjewellery:latest

# Stop the running container
docker stop goodluckjewellery

# Remove the old container
docker rm goodluckjewellery

# Run the new image
docker run -d --name goodluckjewellery -p 8000:8000 sarathkumar455/goodluckjewellery:latest
