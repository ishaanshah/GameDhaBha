BEGIN;

CREATE TABLE Organisations (
   OrganisationID       SERIAL, -- PK
   Name                 TEXT NOT NULL,
   Headquarters         TEXT,
   Founded              DATE NOT NULL,
   Earnings             BIGINT NOT NULL DEFAULT 0
);

CREATE TABLE VideoGame (
   GameID               SERIAL, -- PK
   Name                 TEXT NOT NULL,
   ReleaseDate          DATE NOT NULL,
   LatestPatch          TEXT NOT NULL,
   RegisteredPlayers    BIGINT NOT NULL,
   OrganisationID       INT NOT NULL -- FK to Organisations.OrganisationID
);
ALTER TABLE VideoGame ADD CONSTRAINT user_musicbrainz_id_key UNIQUE (musicbrainz_id);

CREATE TABLE Coach (
   Name                 TEXT NOT NULL,
   StartDate            DATE NOT NULL,
   EndDate              DATE,
   TeamID               INT NOT NULL, -- FK to Team.OrganisationID
   GameID               INT NOT NULL -- FK to VideoGame.GameID
);

CREATE TABLE Played (
   OrganisationID       INT NOT NULL, -- FK to Organisations.OrganisationID
   EventID              INT NOT NULL, -- FK EsportEvent.EventID
   PlayerID             INT NOT NULL, -- FK Players.PlayerID
   GameID               INT NOT NULL  -- FK VideoGame.GameID
);

CREATE TABLE Player (
   PlayerID             SERIAL, -- PK
   Username             TEXT NOT NULL,
   EventID              INT NOT NULL, -- FK EsportEvent.EventID
   GameID               INT NOT NULL  -- FK VideoGame.GameID
);


COMMIT;
