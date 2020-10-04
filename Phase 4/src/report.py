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
    raise NotImplementedError


def GetEventVideoGames(cur, con):
    """ Gets all the games in an event """
    raise NotImplementedError


def GetEventRanklist(cur, con):
    """ Gets information about the top three teams for an event """
    row = {}
    row["EventID"] = input(
        "Enter the EventID of the event to get the ranklist: ")
    
    # Query to be executed
    query = """SELECT *
                FROM Ranklist
                WHERE EventID = %(EventID)s
            """

    print("\nExecuting")
    print(query)

    # Execute query
    cur.execute(query, row)

    # Print the events
    headers = ["FirstPlace", "SecondPlace",
               "ThirdPlace"]
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
    raise NotImplementedError


def GetCoaches(cur, con):
    """ Gets all the coaches for a team and game """
    row = {}
    row["TeamID"] = input(
        "Enter the TeamID of the team to find the coach for: ")
    row["GameID"] = input(("Enter the GameID of the game to find who coached Team {} to play this game: ").format(row["TeamID"]))

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
    headers = ["Name", "StartDate",
               "EndDate"]
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
