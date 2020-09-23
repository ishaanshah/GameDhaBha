ALTER TABLE VideoGames ADD CONSTRAINT fk_organisation_id FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);

ALTER TABLE Coaches ADD CONSTRAINT fk_team_id FOREIGN KEY (TeamID) REFERENCES Teams(OrganisationID);
ALTER TABLE Coaches ADD CONSTRAINT fk_game_id FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);

ALTER TABLE Played ADD CONSTRAINT fk_organisation_id FOREIGN KEY (OrganisationID) REFERENCES Organisations(OrganisationID);
ALTER TABLE Played ADD CONSTRAINT fk_event_id FOREIGN KEY (EventID) REFERENCES EsportEvents(EventID);
ALTER TABLE Played ADD CONSTRAINT fk_player_id FOREIGN KEY (PlyerID) REFERENCES Players(PlayerID);
ALTER TABLE Played ADD CONSTRAINT fk_game_id FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);

ALTER TABLE Players ADD CONSTRAINT fk_game_id FOREIGN KEY (GameID) REFERENCES VideoGames(GameID);
ALTER TABLE Players ADD CONSTRAINT fk_event_id FOREIGN KEY (EventID) REFERENCES EsportEvents(EventID);
