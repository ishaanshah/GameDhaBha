-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `GameDhaBha`;
CREATE DATABASE `GameDhaBha` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `GameDhaBha`;

DROP TABLE IF EXISTS `Coaches`;
CREATE TABLE `Coaches` (
  `Name` text NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date DEFAULT NULL,
  `TeamID` bigint unsigned NOT NULL,
  `GameID` bigint unsigned NOT NULL,
  KEY `CoachTeamFKey` (`TeamID`),
  KEY `CoachGameFKey` (`GameID`),
  CONSTRAINT `CoachGameFKey` FOREIGN KEY (`GameID`) REFERENCES `VideoGames` (`GameID`),
  CONSTRAINT `CoachTeamFKey` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Coaches` (`Name`, `StartDate`, `EndDate`, `TeamID`, `GameID`) VALUES
('Ash Long',	'2020-09-21',	NULL,	10,	1),
('Tanner Curtis',	'2020-06-20',	NULL,	8,	1),
('Taylor Broomall',	'2020-05-22',	NULL,	9,	1),
('Aleksandar Trifunovic',	'2020-09-08',	NULL,	10,	4);

DROP TABLE IF EXISTS `Developers`;
CREATE TABLE `Developers` (
  `OrganisationID` bigint unsigned NOT NULL,
  `CEO` text NOT NULL,
  UNIQUE KEY `UniqueDevOrgID` (`OrganisationID`),
  CONSTRAINT `DevOrgFKey` FOREIGN KEY (`OrganisationID`) REFERENCES `Organisations` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Developers` (`OrganisationID`, `CEO`) VALUES
(2,	'Nicolo Laurent'),
(3,	'Tim Sweeney'),
(4,	'Gabe Newell'),
(7,	'J. Allen Brack');

DROP TABLE IF EXISTS `ESportEvents`;
CREATE TABLE `ESportEvents` (
  `EventID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `StartDate` date NOT NULL,
  `EndDate` date NOT NULL,
  `PrizePool` bigint NOT NULL,
  PRIMARY KEY (`EventID`),
  UNIQUE KEY `EventID` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `ESportEvents` (`EventID`, `Name`, `StartDate`, `EndDate`, `PrizePool`) VALUES
(1,	'Gamers For Equality Tournament',	'2020-07-08',	'2020-07-09',	185930),
(2,	'ELEAGUE Major: Boston 2018',	'2018-01-12',	'2018-01-28',	1000000);

DROP TABLE IF EXISTS `Organisations`;
CREATE TABLE `Organisations` (
  `OrganisationID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Headquarters` text,
  `Founded` date NOT NULL,
  `Earnings` bigint NOT NULL DEFAULT '0',
  PRIMARY KEY (`OrganisationID`),
  UNIQUE KEY `OrganisationID` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Organisations` (`OrganisationID`, `Name`, `Headquarters`, `Founded`, `Earnings`) VALUES
(1,	'Tencent',	'Shenzhen, China',	'1998-11-11',	17478391794),
(2,	'Riot Games',	'Los Angeles, USA',	'2006-08-31',	535727841),
(3,	'Epic Games',	'Cary, USA',	'1991-01-01',	730385603),
(4,	'Valve Corporation',	'Bellevue, US',	'1996-08-24',	43205739),
(5,	'Bluehole',	'Seoul, South Korea',	'2007-03-01',	46389493),
(6,	'PUBG Corp.',	'Seoul, South Korea',	'2015-01-27',	3864024),
(7,	'Blizzard Entertainment, Inc.',	'Irvine, U.S.',	'1991-02-01',	582304953),
(8,	'100 Thieves',	'United States',	'2020-06-04',	1948),
(9,	'Team SoloMid',	'United States',	'2009-09-22',	73347),
(10,	'Cloud9',	'United States',	'2020-04-12',	20500);

DROP TABLE IF EXISTS `Organised`;
CREATE TABLE `Organised` (
  `OrganisationID` bigint unsigned NOT NULL,
  `EventID` bigint unsigned NOT NULL,
  KEY `OrganisedOrgFKey` (`OrganisationID`),
  KEY `OrganisedEventFKey` (`EventID`),
  CONSTRAINT `OrganisedEventFKey` FOREIGN KEY (`EventID`) REFERENCES `ESportEvents` (`EventID`),
  CONSTRAINT `OrganisedOrgFKey` FOREIGN KEY (`OrganisationID`) REFERENCES `Organisations` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Organised` (`OrganisationID`, `EventID`) VALUES
(4,	2),
(8,	1);

DROP TABLE IF EXISTS `Owns`;
CREATE TABLE `Owns` (
  `ParentID` bigint unsigned NOT NULL,
  `SubsidiaryID` bigint unsigned NOT NULL,
  `AcquiredOn` date NOT NULL,
  KEY `ParentOrgFKey` (`ParentID`),
  KEY `SubsidiaryOrgFKey` (`SubsidiaryID`),
  CONSTRAINT `ParentOrgFKey` FOREIGN KEY (`ParentID`) REFERENCES `Organisations` (`OrganisationID`),
  CONSTRAINT `SubsidiaryOrgFKey` FOREIGN KEY (`SubsidiaryID`) REFERENCES `Organisations` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Owns` (`ParentID`, `SubsidiaryID`, `AcquiredOn`) VALUES
(5,	6,	'2015-01-27'),
(1,	2,	'2011-02-01');

DROP TABLE IF EXISTS `Platforms`;
CREATE TABLE `Platforms` (
  `GameID` bigint unsigned NOT NULL,
  `Platform` text NOT NULL,
  KEY `PlatformGameFKey` (`GameID`),
  CONSTRAINT `PlatformGameFKey` FOREIGN KEY (`GameID`) REFERENCES `VideoGames` (`GameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Platforms` (`GameID`, `Platform`) VALUES
(1,	'Microsoft Windows'),
(2,	'Microsoft Windows'),
(2,	'Nintendo Switch'),
(2,	'PlayStation 4'),
(4,	'Xbox One'),
(2,	'iOS'),
(3,	'Microsoft Windows'),
(3,	'Linux'),
(4,	'Microsoft Windows'),
(4,	'PlayStation 3'),
(4,	'Xbox 360'),
(5,	'Microsoft Windows'),
(5,	'PlayStation 4'),
(5,	'Xbox One'),
(5,	'Nintendo Switch');

DROP TABLE IF EXISTS `Played`;
CREATE TABLE `Played` (
  `OrganisationID` bigint unsigned NOT NULL,
  `EventID` bigint unsigned NOT NULL,
  `PlayerID` bigint unsigned NOT NULL,
  `GameID` bigint unsigned NOT NULL,
  UNIQUE KEY `UniquePlayed` (`OrganisationID`,`EventID`,`PlayerID`,`GameID`),
  KEY `PlayedEventFKey` (`EventID`),
  KEY `PlayedPlayerFKey` (`PlayerID`),
  KEY `PlayedGameFKey` (`GameID`),
  CONSTRAINT `PlayedEventFKey` FOREIGN KEY (`EventID`) REFERENCES `ESportEvents` (`EventID`),
  CONSTRAINT `PlayedGameFKey` FOREIGN KEY (`GameID`) REFERENCES `VideoGames` (`GameID`),
  CONSTRAINT `PlayedOrgFKey` FOREIGN KEY (`OrganisationID`) REFERENCES `Teams` (`OrganisationID`),
  CONSTRAINT `PlayedPlayerFKey` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Played` (`OrganisationID`, `EventID`, `PlayerID`, `GameID`) VALUES
(8,	1,	1,	1),
(8,	1,	9,	1),
(8,	1,	10,	1),
(8,	1,	11,	1),
(8,	1,	12,	1),
(9,	1,	4,	1),
(9,	1,	5,	1),
(9,	1,	6,	1),
(9,	1,	7,	1),
(9,	1,	8,	1),
(10,	1,	13,	1),
(10,	1,	14,	1),
(10,	1,	15,	1),
(10,	1,	16,	1),
(10,	1,	17,	1),
(8,	2,	1,	1),
(8,	2,	9,	1),
(8,	2,	10,	1),
(8,	2,	11,	1),
(8,	2,	12,	1),
(9,	2,	4,	1),
(9,	2,	5,	1),
(9,	2,	6,	1),
(9,	2,	7,	1),
(9,	2,	8,	1),
(10,	2,	13,	1),
(10,	2,	14,	1),
(10,	2,	15,	1),
(10,	2,	16,	1),
(10,	2,	17,	1);

DROP TABLE IF EXISTS `Players`;
CREATE TABLE `Players` (
  `Username` varchar(40) NOT NULL,
  `PlayerID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `Winnings` bigint NOT NULL DEFAULT '0',
  `Nationality` text NOT NULL,
  `DateOfBirth` date NOT NULL,
  PRIMARY KEY (`PlayerID`),
  UNIQUE KEY `PlayerID` (`PlayerID`),
  UNIQUE KEY `UniqueUsername` (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Players` (`Username`, `PlayerID`, `FirstName`, `LastName`, `Winnings`, `Nationality`, `DateOfBirth`) VALUES
('hiko',	1,	'Spencer',	'Martin',	162483,	'United States',	'1990-03-06'),
('shroud',	2,	'Michael',	'Grzesiek',	218113,	'Canada',	'1994-06-02'),
('Ninja',	3,	'Richard',	'Blevins',	15028473,	'United States',	'1991-06-05'),
('Wardell',	4,	'Matthew',	'Yu',	56244,	'Canada',	'1998-07-05'),
('hazed',	5,	'James',	'Cobb',	93957,	'United States',	'1989-05-22'),
('drone',	6,	'Taylor',	'Johnson',	14210,	'United States',	'1997-08-29'),
('Subroza',	7,	'Yassine',	'Taoufik',	71729,	'Morocco',	'1997-07-06'),
('reltuC',	8,	'Stephen',	'Cutler',	100510,	'United States',	'1988-11-27'),
('nitr0',	9,	'Nicholas',	'Cannella',	48229,	'United States',	'1995-08-16'),
('steel',	10,	'Joshua',	'Nissan',	43257,	'United Kingdom',	'1989-12-28'),
('Asuna',	11,	'Peter',	'Mazuryk',	3520,	'Ukraine',	'2003-07-26'),
('diceyzx',	12,	'Quan',	'Tran',	1930,	'United States',	'2003-10-05'),
('TenZ',	13,	'Tyson',	'Ngo',	4350,	'Canada',	'2001-05-05'),
('Relyks',	14,	'Skyler',	'Weaver',	4350,	'United States',	'1995-01-12'),
('mitch',	15,	'Mitch',	'Semago',	4350,	'United States',	'1996-07-31'),
('shinobi',	16,	'Josh',	'Abastado',	4350,	'United States',	'1994-06-23'),
('vice',	17,	'Daniel',	'Kim',	4080,	'United States',	'1998-01-01');

DROP TABLE IF EXISTS `Ranklist`;
CREATE TABLE `Ranklist` (
  `EventID` bigint unsigned NOT NULL,
  `FirstPlace` int NOT NULL,
  `SecondPlace` int NOT NULL,
  `ThirdPlace` int NOT NULL,
  KEY `RankEventFKey` (`EventID`),
  CONSTRAINT `RankEventFKey` FOREIGN KEY (`EventID`) REFERENCES `ESportEvents` (`EventID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Ranklist` (`EventID`, `FirstPlace`, `SecondPlace`, `ThirdPlace`) VALUES
(1,	10,	9,	8),
(2,	8,	10,	9);

DROP TABLE IF EXISTS `Teams`;
CREATE TABLE `Teams` (
  `OrganisationID` bigint unsigned NOT NULL,
  `Manager` text NOT NULL,
  UNIQUE KEY `UniqueTeamOrgID` (`OrganisationID`),
  CONSTRAINT `TeamOrgFKey` FOREIGN KEY (`OrganisationID`) REFERENCES `Organisations` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Teams` (`OrganisationID`, `Manager`) VALUES
(8,	'Matthew Haag'),
(9,	'Andy Dinh'),
(10,	'Jack Etienne');

DROP TABLE IF EXISTS `VideoGames`;
CREATE TABLE `VideoGames` (
  `GameID` bigint unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(128) NOT NULL,
  `ReleaseDate` date NOT NULL,
  `LatestPatch` text NOT NULL,
  `RegisteredPlayers` bigint NOT NULL,
  `OrganisationID` bigint unsigned NOT NULL,
  PRIMARY KEY (`GameID`),
  UNIQUE KEY `GameID` (`GameID`),
  UNIQUE KEY `UniqueGameName` (`Name`),
  KEY `GameOrgFKey` (`OrganisationID`),
  CONSTRAINT `GameOrgFKey` FOREIGN KEY (`OrganisationID`) REFERENCES `Developers` (`OrganisationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `VideoGames` (`GameID`, `Name`, `ReleaseDate`, `LatestPatch`, `RegisteredPlayers`, `OrganisationID`) VALUES
(1,	'Valorant',	'2020-06-02',	'1.09',	8349359,	2),
(2,	'Fortnite',	'2017-06-25',	'10.40.1',	64566483,	3),
(3,	'DOTA 2',	'2013-07-09',	'7.27d',	11618862,	4),
(4,	'Counter-Strike: Global Offensive',	'2012-08-21',	'2020.09.17',	24753404,	4),
(5,	'Overwatch',	'2016-05-24',	'SEPTEMBER 29, 2020',	19185813,	7);

-- 2020-10-05 15:24:40