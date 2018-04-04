#!/bin/bash
# A quick start script for building container and start the container.
# You can reach the omireiver container on http://127.0.0.1:8000

echo 
echo Building docker container
echo 

sudo docker build -t alert2omi:latest .

echo 
echo start container
echo

sudo docker run --rm --name alert2omi --link omireceiver:omireceiver -p 5000:5000 alert2omi:latest

