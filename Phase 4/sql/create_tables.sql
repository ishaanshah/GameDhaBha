BEGIN;

CREATE TABLE Organisations (
   OrganisationID       SERIAL, -- PK
   Name                 TEXT NOT NULL,
   Headquarters         TEXT,
   Founded              DATE NOT NULL,
   Earnings             BIGINT NOT NULL DEFAULT 0
);

CREATE TABLE VideoGames (
   GameID               SERIAL, -- PK
   Name                 VARCHAR(128) NOT NULL,
   ReleaseDate          DATE NOT NULL,
   LatestPatch          TEXT NOT NULL,
   RegisteredPlayers    BIGINT NOT NULL,
   OrganisationID       INT NOT NULL -- FK to Organisations.OrganisationID
);
ALTER TABLE VideoGames ADD CONSTRAINT UniqueGameName UNIQUE (Name);

CREATE TABLE Coaches (
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

CREATE TABLE Players (
    Username            VARCHAR(40) NOT NULL,
    PlayerID            SERIAL, -- PK
    FirstName           TEXT NOT NULL,
    LastName            TEXT NOT NULL,
    Winnings            BIGINT NOT NULL DEFAULT 0,
    Nationality         TEXT NOT NULL,
    DateOfBirth         DATE NOT NULL
);
ALTER TABLE Players ADD CONSTRAINT UniqueUsername UNIQUE (Username);

CREATE TABLE Organised (
   OrganisationID       INT NOT NULL, -- FK Organisations.OrganisationID
   EventID              INT NOT NULL -- FK EsportEvent.EventID
);

CREATE TABLE Teams (
   OrganisationID       INT NOT NULL, -- FK to Organisations.OrganisationID
   Manager              TEXT NOT NULL
);

CREATE TABLE Ranklist (
   EventID              INT NOT NULL, -- FK to EsportEvent.EventID
   FirstPlace           INT NOT NULL,
   SecondPlace          INT NOT NULL,
   ThirdPlace           INT NOT NULL
);

CREATE TABLE ESportEvents (
    EventID             SERIAL, -- PK
    Name                TEXT,
    StartDate           DATE NOT NULL,
    EndDate             DATE NOT NULL,
    PrizePool           BIGINT NOT NULL
);

CREATE TABLE Developers (
    OrganizationID      INT NOT NULL, -- FK Organisations.OrganisationID
    CEO                 TEXT NOT NULL
);

CREATE TABLE Owns (
  ParentID          INT NOT NULL, -- FK Organisations.OrganisationID
  SubsidiaryID      INT NOT NULL, -- FK Organisations.OrganisationID
  AcquiredOn        DATE NOT NULL
);

CREATE TABLE Platforms (
  GameID        INT NOT NULL, -- FK VideoGames.GameID
  Platform      TEXT NOT NULL
);

COMMIT;
