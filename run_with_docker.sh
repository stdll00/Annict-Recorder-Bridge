#!/bin/sh
export ANNICT_TOKEN=""
export ENDPOINT=""
export ANNICT_TOKEN="7Vt5sEE2scAZeYm5H6y3e7NAQimeblGfpRS5T3r4v2g"
export ENDPOINT="http://shinapuri.local"

docker pull ghcr.io/stdll00/annict-recorder-bridge:latest # "-aarch64" for arm64
docker run --rm -e annict_token=$ANNICT_TOKEN -e endpoint=$ENDPOINT \
      ghcr.io/stdll00/annict-recorder-bridge:latest
