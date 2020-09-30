#!/bin/bash

if [[ "$1" == mysql ]]; then shift
    echo "Connecting to MySQL..."
    exec docker-compose run --rm db mysql GameDhaBha -P 3306 -h db -u root -ppassword "$@"
elif [[ "$1" == init_db ]]; then shift
    echo "Initialising DB..."
    docker-compose run --rm db mysql -P 3306 -h db -u root -ppassword < sql/create_database.sql
    docker-compose run --rm db mysql GameDhaBha -P 3306 -h db -u root -ppassword < sql/create_tables.sql
    docker-compose run --rm db mysql GameDhaBha -P 3306 -h db -u root -ppassword < sql/create_primary_keys.sql
elif [[ "$1" == drop_db ]]; then shift
    echo "Dropping DB..."
    docker-compose run --rm db mysql GameDhaBha -P 3306 -h db -u root -ppassword < sql/drop_database.sql
else
    echo "Running docker-compose with the given command..."
    exec docker-compose "$@"
fi
