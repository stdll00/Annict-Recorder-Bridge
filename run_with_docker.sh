#!/bin/sh
export ANNICT_TOKEN="YOUR_TOKEN"
export ENDPOINT="http://localhost"

docker pull ghcr.io/stdll00/annict-recorder-bridge:latest
docker run --rm -e annict_token=$ANNICT_TOKEN -e endpoint=$ENDPOINT \
      ghcr.io/stdll00/annict-recorder-bridge:latest
