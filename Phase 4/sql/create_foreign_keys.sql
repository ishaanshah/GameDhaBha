BEGIN;

ALTER TABLE VideoGames ADD CONSTRAINT GameOrgFKey FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);

ALTER TABLE Coaches ADD CONSTRAINT CoachTeamFKey FOREIGN KEY (TeamID) REFERENCES Teams(OrganisationID);
ALTER TABLE Coaches ADD CONSTRAINT CoachGameFKey FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);

ALTER TABLE Played ADD CONSTRAINT PlayedOrgFKey FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);
ALTER TABLE Played ADD CONSTRAINT PlayedEventFKey FOREIGN KEY (EventID) REFERENCES ESportEvents(EventID);
ALTER TABLE Played ADD CONSTRAINT PlayedPlayerFKey FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID);
ALTER TABLE Played ADD CONSTRAINT PlayedGameFKey FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);

ALTER TABLE Organised ADD CONSTRAINT OrganisedOrgFKey FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);
ALTER TABLE Organised ADD CONSTRAINT OrganisedEventFKey FOREIGN KEY (EventID) REFERENCES ESportEvents(EventID);

ALTER TABLE Ranklist ADD CONSTRAINT RankEventFKey FOREIGN KEY (EventID) REFERENCES ESportEvents(EventID);

ALTER TABLE Developers ADD CONSTRAINT DevOrgFKey FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);

ALTER TABLE Teams ADD CONSTRAINT TeamOrgFKey FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);

ALTER TABLE Owns ADD CONSTRAINT ParentOrgFKey FOREIGN KEY (ParentID) REFERENCES Organisations(OrganisationID);
ALTER TABLE Owns ADD CONSTRAINT SubsidiaryOrgFKey FOREIGN KEY (SubsidiaryID) REFERENCES Organisations(OrganisationID);

ALTER TABLE Platforms ADD CONSTRAINT PlatformGameFKey FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);

COMMIT;
