BEGIN;

ALTER TABLE Organisations ADD CONSTRAINT OrganisationsPKey PRIMARY KEY (OrganisationID);

ALTER TABLE VideoGames ADD CONSTRAINT VideoGamesPKey PRIMARY KEY (GameID);

ALTER TABLE Players ADD CONSTRAINT PlayersPKey PRIMARY KEY (PlayerID);

ALTER TABLE ESportEvents ADD CONSTRAINT EventsPKey PRIMARY KEY (EventId);

COMMIT;
