# Data and Applications - Project Phase 4

## Team - RaIS

- Rahul Goel (2019111034)
- Ishaan Shah (2019111028)
- Sriram Devata (2019113007)

## Description

> *Little Timmy was 7 years old. Once, he played the best game ever - Mario Bros. - and he decided that was what he wanted to do when he grew up. However, Little Timmy's Mommy looked down upon playing video games as a profession and scolded him severely, shattering Little Timmy's dreams and his hopes for the future. Little Timmy then started concentrating on his studies and never thought about video games. Or so his mother thought.*

> *Little Timmy has been keeping track of how his favorite players are playing, what video games are being played competitively, the tournaments that are being conducted and any relevant information he might need. One day, Little Timmy will be listed on Gamebrainz. He will show his Mommy his total earnings on the database, and will prove his mother wrong. Video games do earn you money. That will be the day, Little Timmy isn't Little anymore, Little Timmy will be Rich Timmy.*

Traditional sports like Football and Cricket have a huge number of enthusiasts. At this age where everything is being digitalized, enthusiasm for eSports is rising steadily.
In eSports Events, players compete individually or in teams to see who play(s) a video game the best. It is estimated that around half a billion viewers would tune in to watch at least one
eSports Event during 2020. **GameDhaBa** keeps track of these video games, the teams that compete, the players who participate and the organizations that conduct the events in this growing field.

Some of the things users of this database would be able to do is to search for players with the most winnings, see the playerbase for a particular game,
look up organizations that made their favorite game, find the coaches who coached the top ranking teams and many more.

## Build Instructions

- We trust that the TAs reading this are all at a respectable age to be able to handle installation bugs themselves and won't be needing the students to help them :P

- Since the project is built using docker-compose so that needs to be installed using your favourite package manager.

- Make sure that docker is enabled
```
sudo systemctl start docker
```

- You'll need to start the mysql server using
```
./develop.sh up

```
- In case you want to run a new instance of the same database, drop the database and re-initialise it.
```
./develop.sh drop_db
```

- Initialise the database using
```
./develop.sh init_db
```

- To use the sample data, run
```
./develop.sh mysql < sql/dump.sql
```

- Install the python requirements using
```
pip install -r requirements.txt
```

- To open the CLI, run
```
python app.py
```
