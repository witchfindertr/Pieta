#!/bin/bash
echo -e '\e[5mInstalling..\e[0m' && apt-get update && apt upgrade -y && apt install gcc && apt install g++ && apt install g++-mingw-w64-i686 && pip3 install -r requirements.txt && chmod +x /opt/pieta
echo "Run Pieta to get started"
