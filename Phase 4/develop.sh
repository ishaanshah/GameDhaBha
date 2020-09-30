#!/bin/bash

if [[ "$1" == mysql ]]; then shift
    echo "Connecting to MySQL..."
    exec docker-compose run --rm db mysql GameDhaBha -P 3306 -h db -u root -ppassword "$@"
else
    echo "Running docker-compose with the given command..."
    exec docker-compose "$@"
fi
