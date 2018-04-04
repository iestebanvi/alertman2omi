#!/bin/bash
# A quick start script for building container and start the container.
# You can reach the omireiver container on http://127.0.0.1:8000

echo 
echo Building docker container
echo 

sudo docker build -t omireceiver:latest .

echo 
echo start container
echo

sudo docker run --name omireceiver --rm -p 8000:5000 omireceiver:latest

