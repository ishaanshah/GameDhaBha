""" Contains all the functions related to report generation """

from tabulate import tabulate


def GetGamesByDeveloper(cur, con):
    """ Gets all the games made by a developer """
    row = {}
    row["DeveloperID"] = input(
        "Enter the DeveloperID of the developer to get the games for: ") or None

    # Query to be executed
    query = """SELECT *
                 FROM VideoGames
                WHERE OrganisationID = %(DeveloperID)s
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the events
    headers = ["GameID", "Name", "ReleaseDate",
               "LatestPatch", "RegisteredPlayers"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def GetTeamParticipation(cur, con):
    """ Gets all the events that a team has participated in """
    raise NotImplementedError


def GetEventTeams(cur, con):
    """ Gets all the teams participating in an event """
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the event to get the "
        "list of teams in the event: ") or None

    # Query to be executed
    query = """
            WITH TeamsList (TeamID)
              AS (
                SELECT DISTINCT OrganisationID
                  FROM Played
                 WHERE EventID = %(EventID)s
              )
            SELECT TeamsList.TeamID,
                   Organisations.Name AS TeamName
              FROM TeamsList
              JOIN Organisations
                ON TeamsList.TeamID = Organisations.OrganisationID
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the Teams
    headers = ["TeamID", "TeamName"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def GetEventVideoGames(cur, con):
    """ Gets all the games in an event """
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the event to get the "
        "list of games in the event: ") or None

    # Query to be executed
    query = """
            WITH GamesInEvent (GameID)
              AS (
                SELECT DISTINCT GameID
                  FROM Played
                 WHERE EventID = %(EventID)s
              )
            SELECT VideoGames.GameID,
                   VideoGames.Name AS VideoGameName
              FROM GamesInEvent
              JOIN VideoGames
                ON GamesInEvent.GameID = VideoGames.GameID
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the Games
    headers = ["GameID", "VideoGameName"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def GetEventRanklist(cur, con):
    """ Gets information about the top three teams for an event """
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the event to get the ranklist: ")

    # Query to be executed
    query = """WITH Placements (Position, TeamID)
                 AS (
                   SELECT "FirstPlace" AS Position,
                          FirstPlace AS TeamID
                     FROM Ranklist
                    WHERE EventID = %(EventID)s
                   UNION ALL
                   SELECT "SecondPlace" AS Position,
                          SecondPlace AS TeamID
                     FROM Ranklist
                    WHERE EventID = %(EventID)s
                   UNION ALL
                   SELECT "ThirdPlace" AS Position,
                          ThirdPlace AS TeamID
                     FROM Ranklist
                    WHERE EventID = %(EventID)s
                 )
               SELECT Placements.Position,
                      Organisations.*,
                      Teams.Manager
                 FROM Teams
                 JOIN Placements
                   ON Placements.TeamID = Teams.OrganisationID
                 JOIN Organisations
                   ON Teams.OrganisationID = Organisations.OrganisationID
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the Ranklist
    headers = ["Position", "OrganisationID", "Manager", "Name",
               "Headquarters", "Founded", "Earnings"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def GetPlayerTeams(cur, con):
    """ Gets all the teams that the player is a part of """
    row = {}
    row["PlayerID"] = input(
        "Enter the PlayerID of the player to find the "
        "teams the player is/was a part of: ") or None

    # Query to be executed
    query = """WITH PlayerTeamIDs (TeamID)
                 AS (
                    SELECT DISTINCT OrganisationID
                      FROM Played
                     WHERE PlayerID = %(PlayerID)s
                  )
                SELECT PlayerTeamIDs.TeamID,
                       Organisations.Name AS TeamName
                  FROM PlayerTeamIDs
                  JOIN Organisations
                    ON PlayerTeamIDs.TeamID = Organisations.OrganisationID
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the Teams
    headers = ["TeamID", "TeamName"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def GetCoaches(cur, con):
    """ Gets all the coaches for a team and game """
    row = {}
    row["TeamID"] = input(
        "Enter the TeamID of the team to find the coach for: ") or None
    row["GameID"] = input(
        "Enter the GameID of the game to find who coached "
        f"Team {row['TeamID']} to play this game: ") or None

    # Query to be executed
    query = """SELECT *
                 FROM Coaches
                WHERE TeamID = %(TeamID)s
                  AND GameID = %(GameID)s
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the coaches
    headers = ["Name", "StartDate", "EndDate"]
    rows = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        rows.append([res[header] for header in headers])

    print(tabulate(rows, headers=headers, tablefmt="orgtbl"))
    print("")


def ReportHandler(cur, con):
    # Define handlers
    handlers = [
        GetGamesByDeveloper,
        GetTeamParticipation,
        GetEventTeams,
        GetEventVideoGames,
        GetEventRanklist,
        GetPlayerTeams,
        GetCoaches
    ]

    # Get operation to perform
    print("1. Get games made by a developer")
    print("2. Get events that teams are taking part in")
    print("3. Get teams participating in an event")
    print("4. Get video games played in an event")
    print("5. Get ranklist for an event")
    print("6. Get teams that player is and has been a part of")
    print("7. Get all coaches for a team and game")
    print("8. Go Back")
    ch = int(input("Enter choice: "))
    if ch == 8:
        return

    try:
        handlers[ch-1](cur, con)
        con.commit()
        print("Report generation successful")
    except (IndexError, TypeError) as error:
        print(f"Error: Invalid option {ch}")
        print(error)
    except Exception as error:
        con.rollback()
        print("Failed to retrieve data form the Database")
        print(f"Error: {error}")
